"""DICOM web storage module."""
import re
import tempfile
import typing as t
from datetime import datetime, timezone
from distutils.util import strtobool
from pathlib import Path

import pydicom
import urllib3
from fw_file.dicom.utils import get_timestamp
from fw_http_client import AnyAuth, HttpClient, HttpConfig
from fw_utils import Filters, fileglob
from pydicom.dataset import Dataset

from .. import __version__
from ..fileinfo import FileInfo
from ..storage import AnyPath, Storage, convert_to_path

__all__ = ["DICOMweb"]

client_info = dict(client_name="fw-storage", client_version=__version__)

UID_RE = r"\d+[\.\d+]*"
PATH_RE_OPTIONAL = fr"^((?P<study>{UID_RE})(/(?P<series>{UID_RE}))?)?$"
PATH_RE_REQUIRED = fr"(?P<study>{UID_RE})/(?P<series>{UID_RE})"


class DICOMweb(Storage):
    """Storage class for web-based medical imaging."""

    url_re = re.compile(
        r"dicomweb://((?P<auth>[^@]+)@)?(?P<url>[^\?]+)(\?(?P<query>[^#]+))?"
    )

    def __init__(
        self,
        url: str,
        secure: str = "True",
        auth: t.Optional[AnyAuth] = None,
    ) -> None:
        """Construct DICOM web storage."""
        url = f"https://{url}" if bool(strtobool(secure)) else f"http://{url}"
        if isinstance(auth, str) and ":" in auth:
            auth = tuple(auth.split(":", 1))
        config = HttpConfig(baseurl=url, auth=auth, **client_info)
        self.client = DICOMwebClient(config=config)

    def abspath(self, path: AnyPath) -> str:
        """Return absolute path for a given path."""
        raise NotImplementedError

    def ls(
        self, path: str = "", *, include: Filters = None, exclude: Filters = None, **_
    ) -> t.Iterator[FileInfo]:
        """Yield items under path that match the include/exclude filters."""
        query: dict = {
            "includefield": [
                "NumberOfSeriesRelatedInstances",
                "SeriesDate",
                "SeriesTime",
            ]
        }
        match = re.match(PATH_RE_OPTIONAL, path)
        if not match:
            raise ValueError(f"Invalid DICOM study/series path: {path}")
        if include:
            inc_filters = parse_filters(include)
            query.update(inc_filters)
        if exclude:
            exc_filters = parse_filters(exclude)
            query["includefield"].extend(list(exc_filters.keys()))
        study_uid = match.group("study")
        series_uid = match.group("series")
        if study_uid and series_uid:
            query.update({"SeriesInstanceUID": series_uid})
            result = self.client.qido(f"/studies/{study_uid}/series", params=query)
            if result:
                if exclude and apply_exclude_filters(result[0], exc_filters):
                    return
                yield result_to_fileinfo(result[0])
            return
        if study_uid:
            study_uids = [study_uid]
        else:
            study_uids = [ds.StudyInstanceUID for ds in self.client.qido("/studies")]
        for study_uid in study_uids:
            for ds in self.client.qido(f"/studies/{study_uid}/series", params=query):
                if exclude and apply_exclude_filters(ds, exc_filters):
                    continue
                yield result_to_fileinfo(ds)

    def stat(self, path: str) -> FileInfo:
        """Return FileInfo for a single file."""
        raise NotImplementedError

    def get(self, path: AnyPath, **kwargs: t.Any) -> AnyPath:  # type: ignore
        """Return a path pointing to the downloaded series."""
        series_path = convert_to_path(path)
        match = re.match(PATH_RE_REQUIRED, str(series_path))
        if not match:
            raise ValueError(f"Invalid DICOM study/series path: {series_path}")
        study_uid = match.group("study")
        series_uid = match.group("series")
        parts = self.client.wado(f"/studies/{study_uid}/series/{series_uid}")
        tmp = Path(tempfile.gettempdir()) / series_path
        tmp.mkdir(parents=True, exist_ok=True)
        for index, part in enumerate(parts):
            with open(f"{tmp}/{index + 1:05}.dcm", "wb") as f:
                f.write(part.content)
        return str(tmp)

    def set(self, file: AnyPath) -> None:  # type: ignore
        """Write a file at the given path in storage."""
        # pylint: disable=arguments-differ
        path = convert_to_path(file)
        paths = []
        if path.is_dir():
            paths.extend(list(fileglob(path)))
        else:
            paths.append(path)
        boundary = urllib3.filepost.choose_boundary()
        headers = {
            "Content-Type": (
                "multipart/related; " "type=application/dicom; " f"boundary={boundary}"
            )
        }
        parts = get_instances_bytes(paths)
        content = multi_encode(parts, boundary)
        self.client.post("/studies", data=content, headers=headers)

    def rm(self, path: AnyPath, recurse: bool = False) -> None:
        """Remove file from storage."""
        raise NotImplementedError


class DICOMwebClient(HttpClient):
    def qido(self, url, params=None):
        """Handle QIDO requests."""
        headers = {"Accept": "application/json"}
        response = super().get(url, raw=True, params=params, headers=headers)
        content_type = response.headers.get("Content-Type")
        datasets = []
        if content_type in ["application/json", "application/dicom+json"]:
            for ds in response.json():
                datasets.append(Dataset.from_json(ds))
        return datasets

    def wado(self, url):
        """Handle WADO requests."""
        headers = {"Accept": "multipart/related; type=application/dicom;"}
        response = super().get(url, stream=True, headers=headers)
        yield from response.iter_parts()


# TODO: Move to Dicom abstract class later
def parse_filters(filters: t.List[str]) -> t.Dict[str, str]:
    """Parse list of strings into filter dict."""
    filt_dict = {}
    for filt in filters:
        try:
            key, value = filt.split("=", maxsplit=1)
            filt_dict[key] = value
        except ValueError as exc:
            raise ValueError("Missing filter key or value") from exc
    return filt_dict


# TODO: Move to Dicom abstract class later
def apply_exclude_filters(ds: Dataset, filters: t.Dict[str, str]) -> bool:
    """Apply exclude filters on dataset."""
    for key, value in filters.items():
        field = ds.get(int(param_to_tag(key), 16))
        if field is None:
            continue
        if field.VR in ("DA", "TM"):
            if "-" in value:
                minimum, maximum = value.split("-")
                if minimum <= field.value <= maximum:
                    return True
        elif field.VR == "UI":
            if "," in value:
                if field.value in value.split(","):
                    return True
        if field.value == value:
            return True
    return False


# TODO: Move to Dicom abstract class later
def param_to_tag(param: str) -> str:
    """Get DICOM tag string for query param."""
    if param in pydicom.datadict.keyword_dict:
        tag = f"{pydicom.datadict.tag_for_keyword(param):08x}"
    else:
        tag = param
    pydicom.datadict.keyword_for_tag(tag)
    return tag


def get_instances_bytes(paths: t.List[Path]) -> t.Iterator[bytes]:
    """Yield bytes of an instance from file."""
    for path in paths:
        yield open(path, mode="rb").read()


def multi_encode(
    parts: t.Iterator[bytes], boundary: str, encoding: str = "utf-8"
) -> t.Iterator[bytes]:
    """Yield HTTP multipart message parts."""
    b_crlf = "\r\n".encode(encoding)
    b_boundary = f"--{boundary}".encode(encoding)
    b_boundary_end = f"--{boundary}--".encode(encoding)
    b_media_type = "Content-Type: application/dicom".encode(encoding)
    b_part_header = b"".join([b_boundary, b_crlf, b_media_type, b_crlf, b_crlf])
    for part in parts:
        yield b"".join([b_part_header, part, b_crlf])
    yield b"".join([b_boundary_end, b_crlf, b_crlf])


# TODO: Move to Dicom abstract class later
def result_to_fileinfo(ds: Dataset) -> FileInfo:
    """Fills the FileInfo from a dict."""
    study_uid = ds.StudyInstanceUID
    series_uid = ds.SeriesInstanceUID
    size = ds.get("NumberOfSeriesRelatedInstances", 0)
    dt = get_timestamp(ds, "Series")
    if dt:
        timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
    else:
        timestamp = datetime.utcnow().timestamp()
    return FileInfo(
        path=f"{study_uid}/{series_uid}",
        size=size,
        created=timestamp,
        modified=timestamp,
    )
