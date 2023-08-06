"""DICOM storage module."""
import re
import typing as t

import pydicom
from fw_utils import Filters, fileglob
from pydicom.dataset import Dataset
from pynetdicom import AE, StoragePresentationContexts, sop_class

from ..fileinfo import FileInfo
from ..storage import AnyPath, Storage, convert_to_path
from .dicomweb import apply_exclude_filters, param_to_tag
from .dicomweb import parse_filters as parse_filters_to_dict
from .dicomweb import result_to_fileinfo

__all__ = ["DICOM"]

UID_RE = r"\d+[\.\d+]*"
PATH_RE_OPTIONAL = fr"^((?P<study>{UID_RE})(/(?P<series>{UID_RE}))?)?$"

PENDING = {0xFF00, 0xFF01}
SUCCESS = 0x0000

STUDY_FIND = (
    sop_class.StudyRootQueryRetrieveInformationModelFind  # pylint: disable=no-member
)


class DICOM(Storage):
    """Storage class for medical imaging."""

    url_re = re.compile(
        r"dicom://"
        r"((?P<aet>[^:@]+)(:(?P<rport>[^@]\d+))?@)?"
        r"(?P<host>[^:]+):(?P<port>\d+)"
        r"(/(?P<aec>.+))?"
    )

    def __init__(
        self,
        host: str,
        port: str,
        aec: t.Optional[str] = None,
        aet: str = "FW-STORAGE",
        rport: t.Optional[str] = None,
    ) -> None:
        """Construct DICOM storage.

        Args:
            host: DICOM SCP / PACS server host or IP.
            port: DICOM SCP / PACS server port.
            aec: Called Application Entity Title.
            aet: Calling Application Entity Title.
            rport: Return port for moving images (C-MOVE).
        """
        # pylint: disable=too-many-arguments
        self.ae = AE(ae_title=aet.encode())
        self.ae.add_requested_context(STUDY_FIND)
        for cx in StoragePresentationContexts:
            if len(self.ae.requested_contexts) == 128:
                break
            self.ae.add_requested_context(cx.abstract_syntax)
        self.rport = int(rport) if rport else None
        self.assoc = self.ae.associate(host, int(port), ae_title=aec or b"ANY-SCP")

    def cleanup(self):
        """Abort association."""
        if not self.assoc.is_aborted:
            self.assoc.abort()

    def ls(
        self, path: str = "", *, include: Filters = None, exclude: Filters = None, **_
    ) -> t.Iterator[FileInfo]:
        """Yield items under path that match the include/exclude filters."""
        ds = Dataset()
        ds.QueryRetrieveLevel = "SERIES"
        ds.SeriesInstanceUID = None
        ds.SeriesDate = None
        ds.SeriesTime = None
        ds.NumberOfSeriesRelatedInstances = None
        match = re.match(PATH_RE_OPTIONAL, path)
        if not match:
            raise ValueError(f"Invalid DICOM study/series path: {path}")
        study_uid = match.group("study")
        series_uid = match.group("series")
        if include:
            parse_filters_to_ds(include, ds)
        exc_filters = {}
        if exclude:
            exc_filters = parse_filters_to_dict(exclude)
            for key in exc_filters:
                param_to_tag(key)
                setattr(ds, key, None)
        study_uids = [study_uid] if study_uid else self._get_every_study_uid()
        if series_uid:
            ds.SeriesInstanceUID = series_uid
        ds.StudyInstanceUID = study_uids
        responses = self.assoc.send_c_find(ds, STUDY_FIND)
        for resp in iter_scp_responses(responses, exc_filters):
            yield result_to_fileinfo(resp)

    def abspath(self, path: AnyPath) -> str:
        """Return absolute path for a given path."""
        raise NotImplementedError

    def stat(self, path: str) -> FileInfo:
        """Return FileInfo for a single file."""
        raise NotImplementedError

    def get(self, path: AnyPath, **kwargs: t.Any) -> AnyPath:
        """Return a file opened for reading in binary mode."""
        raise NotImplementedError

    def set(self, file: AnyPath) -> None:  # type: ignore
        """Write a file at the given path in storage."""
        # pylint: disable=arguments-differ
        path = convert_to_path(file)
        paths = fileglob(path) if path.is_dir() else [path]
        for path in paths:
            ds = pydicom.dcmread(path)
            self.assoc.send_c_store(ds)

    def rm(self, path: AnyPath, recurse: bool = False) -> None:
        """Remove file from storage."""
        raise NotImplementedError

    def _get_every_study_uid(self):
        """Get every study uid."""
        study_uids = []
        study_ds = Dataset()
        study_ds.QueryRetrieveLevel = "STUDY"
        study_ds.StudyInstanceUID = None
        for resp in iter_scp_responses(self.assoc.send_c_find(study_ds, STUDY_FIND)):
            study_uids.append(resp.StudyInstanceUID)
        return study_uids


def iter_scp_responses(
    responses: t.Iterator[Dataset], exc_filters: t.Optional[dict] = None
) -> t.Iterator[Dataset]:
    """Process C-FIND response."""
    for status, identifier in responses:
        if not status:
            msg = "Connection error: timed out, aborted or received invalid response"
            raise ValueError(msg)
        if status.Status in PENDING:
            if exc_filters and apply_exclude_filters(identifier, exc_filters):
                continue
            yield identifier
        elif status.Status == SUCCESS:
            return
        else:
            raise ValueError(f"An error occured (DIMSE status: {status})")


def parse_filters_to_ds(filters: t.List[str], ds: Dataset) -> None:
    """Parse list of strings into Dataset filters."""
    for filt in filters:
        try:
            key, value = filt.split("=", maxsplit=1)
            if "," in value:
                setattr(ds, key, value.split(","))
            else:
                setattr(ds, key, value)
        except ValueError as exc:
            raise ValueError("Missing filter key or value") from exc
