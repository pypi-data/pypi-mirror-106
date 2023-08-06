from typing import List, Type

from terality_serde import all_external_types, SerdeMixin, SerdeConfig, CallableWrapper

from . import (
    StructRef, IndexColNames, PandasIndexMetadata, PandasSeriesMetadata, PandasDFMetadata,
    UploadRequest, ExportRequest, ExportResponse, ErrorResponse, TransferConfigLocal,
    PandasFunctionRequest,
    TransferConfig, SessionInfoLocal, SessionInfo, CreateSessionResponse, ComputationResponse, PendingComputationResponse,
    TeralityAuthError, TeralityInternalError,
    DeleteSessionResponse,
    AwsCredentials, DataTransferResponse,
    ImportFromCloudRequest, ImportFromCloudResponse, AwsS3ObjectKey, ImportFromS3Source, ImportFromCloudRequest, AwsPresignedUrlGet, StorageService
)


_types_to_send: List[Type[SerdeMixin]] = [CallableWrapper, IndexColNames, PandasIndexMetadata, PandasSeriesMetadata, PandasDFMetadata,
                                          StructRef, UploadRequest, ExportRequest, PandasFunctionRequest, ImportFromCloudRequest, StorageService, AwsPresignedUrlGet, ImportFromCloudRequest, ImportFromS3Source, AwsS3ObjectKey]
serde_config_client_to_scheduler = SerdeConfig(_types_to_send, all_external_types)

_types_to_receive: List[Type[SerdeMixin]] = [
    IndexColNames, PandasIndexMetadata, PandasSeriesMetadata, PandasDFMetadata, IndexColNames,
    StructRef, ExportResponse, ErrorResponse, TransferConfigLocal, TransferConfig,
    SessionInfoLocal, SessionInfo,
    TeralityAuthError, TeralityInternalError,
    CreateSessionResponse, DeleteSessionResponse, ComputationResponse, PendingComputationResponse,
    AwsCredentials, DataTransferResponse,
    ImportFromCloudResponse
]
serde_config_scheduler_to_client = SerdeConfig(_types_to_receive, all_external_types)
