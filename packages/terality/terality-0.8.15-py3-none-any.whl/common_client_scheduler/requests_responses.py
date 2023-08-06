from __future__ import annotations
from dataclasses import dataclass
from typing import Any, List, Optional, Type, Union

from terality_serde import SerdeMixin, SerializableEnum

from . import TransferConfig, TransferConfigLocal


""" Endpoints requests/responses """


@dataclass
class ErrorResponse(SerdeMixin):
    exception_class: Type
    args: List


@dataclass
class PendingComputationResponse(SerdeMixin):
    pending_computation_id: str


@dataclass
class ComputationResponse(SerdeMixin):
    result: Any
    inplace: bool


@dataclass
class CreateSessionResponse(SerdeMixin):
    id: str
    upload_config: Union[TransferConfig, TransferConfigLocal]
    download_config: Union[TransferConfig, TransferConfigLocal]


@dataclass
class DeleteSessionResponse(SerdeMixin):
    """Response to the delete session endpoint"""
    pass


@dataclass
class Upload(SerdeMixin):
    path: str


@dataclass
class UploadRequest(SerdeMixin):
    transfer_id: str
    aws_region: Optional[str]


@dataclass
class ExportRequest(SerdeMixin):
    path: str
    aws_region: Optional[str]


@dataclass
class ExportResponse(SerdeMixin):
    path: str
    aws_region: Optional[str]
    is_folder: bool
    transfer_id: str


@dataclass
class AwsCredentials(SerdeMixin):
    access_key_id: str
    secret_access_key: str
    session_token: str


@dataclass
class DataTransferResponse(SerdeMixin):
    temporary_upload_aws_credentials: AwsCredentials


class StorageService(SerializableEnum):
    AWS_S3 = 'AWS_S3'


@dataclass
class AwsPresignedUrlGet(SerdeMixin):
    """A presigned AWS URL allowing to run GetObject on an S3 object part."""
    url: str
    object_key: AwsS3ObjectKey
    # warning, these offsets are inclusive
    range_start_byte: int
    range_end_byte: int


@dataclass(frozen=True, order=True)
class AwsS3ObjectKey(SerdeMixin):
    bucket: str
    key: str


@dataclass
class ImportFromS3Source(SerdeMixin):
    presigned_urls: List[AwsPresignedUrlGet]


@dataclass
class ImportFromCloudRequest(SerdeMixin):
    service: StorageService
    # Will be an Union when we add support for more cloud providers
    source: ImportFromS3Source


@dataclass
class ImportFromCloudResponse(SerdeMixin):
    transfer_id: str
