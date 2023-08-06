import asyncio
from io import BytesIO
from pathlib import Path
from threading import Thread
from typing import Any, Callable, Iterator, List, Tuple, Optional
from uuid import uuid4

import aioboto3
from botocore.client import BaseClient
from botocore.config import Config
import boto3
from common_client_scheduler import AwsCredentials
from common_client_scheduler.requests_responses import AwsPresignedUrlGet, AwsS3ObjectKey, ImportFromCloudRequest, ImportFromS3Source, StorageService

from .. import Connection


#######################################################################################################################
# Utils


class ConfigS3:
    max_conns: int = 1000
    max_retries: int = 1
    connect_timeout: int = 5
    read_timeout: int = 5

    @classmethod
    def config(cls) -> Config:
        return Config(
            max_pool_connections=cls.max_conns,
            retries=dict(max_attempts=cls.max_retries),
            connect_timeout=cls.connect_timeout
        )


def _run_async(func_async: Callable, *args) -> None:
    event_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(event_loop)
    event_loop.run_until_complete(func_async(*args))


def _run_threaded_async(func_async: Callable, *args):
    t = Thread(target=_run_async, args=(func_async, *args))
    t.start()
    t.join()


class _S3:
    # Authentication
    # ~~~~~~~~~~~~~~
    #
    # We use the S3 client in two configurations:
    # * local to S3 copies, or S3 to local copies (where S3 is a Terality owned bucket)
    # * S3 to S3 copies (between a user and a Terality owned bucket)
    #
    # While the user may have her own AWS credentials in her environment, we can't use them to write to
    # Terality buckets. Indeed, regardless of bucket policies, the user won't be able to perform a PutObject
    # (or CreateMultipartUpload) on a Terality bucket without a policy giving him "s3:PutObject" on said
    # bucket. Same goes for reads.
    #
    # Instead, whenever the client needs to perform a write or read operation on a Terality bucket,
    # it retrieves short-lived, temporary AWS credentials from the Terality API suitable for the operation.
    #
    # This is simpler than having the server generate pre-signed URLs, and provides the same level of
    # security.
    #
    # However, Terality-issued credentials can't be used to read or write S3 files to user buckets.
    # Right now, to secure S3-to-S3 copies, we rely on bucket policies and the CopyObject operation with the
    # user credentials, and hope that the user has enough permissions on his AWS credentials
    # ('s3:PutObject and 's3:GetObject' on '*' would do for instance).
    # In a future release, we'll do S3-to-S3 operations server-side, with presigned URLs.
    #
    _client: Any = None
    _client_with_credentials: Any = None
    _credentials: Optional[AwsCredentials] = None

    @classmethod
    def client(cls):
        """An S3 client using user credentials (using the default boto3 loading mecanism).

        Operations with this client will fail if the user has no AWS credentials available in their
        environment.
        """
        if cls._client is None:
            cls._client = boto3.session.Session().client('s3', config=Config(max_pool_connections=200))  # type: ignore
        return cls._client

    @classmethod
    def client_from_credentials(cls, credentials: AwsCredentials):
        """An authenticated S3 client, with temporary credentials provided by Terality."""
        if cls._credentials != credentials:
            cls._client_with_credentials = boto3.session.Session().client(  # type: ignore
                's3', config=Config(max_pool_connections=200),
                aws_access_key_id=credentials.access_key_id,
                aws_secret_access_key=credentials.secret_access_key,
                aws_session_token=credentials.session_token
            )
            cls._credentials = credentials
        return cls._client_with_credentials


_ACL = {'ACL': 'bucket-owner-full-control'}


def _list_keys(bucket: str, key_prefix: str) -> List[str]:
    r = _S3.client().list_objects_v2(Bucket=bucket, Prefix=key_prefix)
    keys = [result['Key'] for result in r['Contents']]
    return keys


#######################################################################################################################

class DataTransfer:
    """
    Various functions to upload and download files to/from S3.

    These functions are defined as class methods to make writing mocks easier during testing.
    """
    @staticmethod
    def upload_bytes(upload_config, aws_credentials: AwsCredentials, data: BytesIO) -> str:
        data.seek(0)
        transfer_id = str(uuid4())
        key = f'{upload_config.key_prefix}{transfer_id}/0.data'
        _S3.client_from_credentials(aws_credentials).upload_fileobj(Fileobj=data, Bucket=upload_config.bucket_region(), Key=key, ExtraArgs=_ACL)
        return transfer_id

    @staticmethod
    def upload_local_file(upload_config, aws_credentials: AwsCredentials, local_file: str, file_suffix: str) -> None:
        key = f'{upload_config.key_prefix}{file_suffix}'
        _S3.client_from_credentials(aws_credentials).upload_file(Bucket=upload_config.bucket_region(), Key=key, Filename=local_file, ExtraArgs=_ACL)

    @staticmethod
    def download_to_bytes(download_config, aws_credentials: AwsCredentials, transfer_id: str) -> BytesIO:
        buf = BytesIO()
        key = f'{download_config.key_prefix}{transfer_id}/0.parquet'
        _S3.client_from_credentials(aws_credentials).download_fileobj(Bucket=download_config.bucket_region(), Key=key, Fileobj=buf)
        return buf

    @staticmethod
    def download_to_local_files(download_config, aws_credentials: AwsCredentials, transfer_id: str, path: str, is_folder: bool) -> None:
        bucket = download_config.bucket_region()
        key_prefix = f'{download_config.key_prefix}{transfer_id}/'
        keys = _list_keys(bucket, key_prefix)
        if is_folder:
            for num, key in enumerate(keys):
                _S3._client_with_credentials(aws_credentials).download_file(Bucket=bucket, Key=key, Filename=path.format(num))
        else:
            _S3._client_with_credentials(aws_credentials).download_file(Bucket=bucket, Key=keys[0], Filename=path)


#######################################################################################################################
# Uploads

def upload_local_files(path: str, transfer_id: str, aws_credentials: AwsCredentials) -> None:
    """
    Copy files from a local directory to a Terality-owned S3 bucket.

    Args:
        path: path to a single file or a directory. If a directory, all files in the directory will be uploaded.
    """
    paths: List[str] = [path] if Path(path).is_file() else [str(path_) for path_ in sorted(Path(path).iterdir())]
    for file_num in range(len(paths)):
        DataTransfer.upload_local_file(Connection.session.upload_config,
                                       aws_credentials,
                                       paths[file_num],
                                       f'{transfer_id}/{file_num}.data')


def upload_s3_files(s3_bucket: str, s3_key_prefix: str) -> str:
    """
    Copy files from a source (user-owner) S3 bucket to a Terality-owned S3 bucket.

    Generate pre-signed URL for each chunk of each object to transfer, then send all these URLs to the
    Terality API. Terality will perform the copy server-side. The user AWS credentials are only used to
    generate these pre-signed URLs and are never sent to Terality.

    Assumes that the user has read permissions on all objects to be copied. Uses the boto3 standard
    credentials discovery mecanism.

    Args:
        s3_bucket: source S3 bucket
        s3_key_prefix: source S3 objects

    Return:
        a transfer ID. This ID can then be used as input to "read_csv/read_parquet" requests.
    """
    client = _S3.client()
    presigned_urls = []
    for s3_key, object_size in _list_all_objects_under_prefix(client, s3_bucket, s3_key_prefix):
        presigned_urls += list(_generate_presigned_urls(client, s3_bucket, s3_key, object_size))
    request = ImportFromCloudRequest(
        service=StorageService.AWS_S3,
        source=ImportFromS3Source(presigned_urls=presigned_urls)
    )
    response = Connection.poll_for_answer("imports/cloud", request)
    return response.transfer_id


def _list_all_objects_under_prefix(client: BaseClient, s3_bucket: str, s3_key_prefix: str) -> Iterator[Tuple[str, int]]:
    """List all S3 keys in a bucket starting with a given prefix.

    Yield:
        tuples of (S3 object key, object size in bytes)
    """
    paginator = client.get_paginator('list_objects_v2')
    page_iterator = paginator.paginate(Bucket=s3_bucket, Prefix=s3_key_prefix)
    for page in page_iterator:
        objects = page['Contents']
        for obj in objects:
            yield (obj['Key'], obj['Size'])


def _generate_presigned_urls(client: BaseClient, s3_bucket: str, s3_key: str, object_size: int, part_size_bytes: int=400*1024*1024) -> Iterator[AwsPresignedUrlGet]:
    """Generate pre-signed URLs allowing to read part of a S3 object.

    This function provides a few guarantees, that the server is relying on:
    * for each object, the URLs cover contiguous byte ranges of this object
    * the URLs are sorted by part number
    """
    range_start_byte = 0
    while range_start_byte < object_size:
        # byte range are inclusive
        range_end_byte = min(range_start_byte + part_size_bytes, object_size) - 1
        expiration = 3600
        url = client.generate_presigned_url(
            'get_object', Params={'Bucket': s3_bucket, 'Key': s3_key}, ExpiresIn=expiration
        )
        yield AwsPresignedUrlGet(
            url=url,
            range_start_byte=range_start_byte,
            range_end_byte=range_end_byte,
            object_key=AwsS3ObjectKey(bucket=s3_bucket, key=s3_key)
        )
        range_start_byte = range_end_byte + 1


#######################################################################################################################
# Downloads


async def _download_to_s3_async(terality_bucket: str, terality_keys: List[str],
                                client_bucket: str, client_key_prefix: str) -> None:
    async with aioboto3.session.Session().client('s3', config=ConfigS3.config()) as s3:
        await asyncio.gather(*[
            s3.copy_object(
                CopySource={'Bucket': terality_bucket, 'Key': terality_key},
                Bucket=client_bucket, Key=client_key_prefix.format(key_num),
                # SSECustomerAlgorithm='AES256',
            )
            for key_num, terality_key in enumerate(terality_keys)
        ])


def download_to_s3_files(transfer_id: str, aws_region: str, destination_s3_path: str) -> None:
    download_config = Connection.session.download_config
    bucket = download_config.bucket_region(aws_region)
    terality_keys = _list_keys(bucket, f'{download_config.key_prefix}{transfer_id}/')
    client_bucket, client_key_prefix = destination_s3_path[5:].split('/', 1)
    _run_threaded_async(_download_to_s3_async, bucket, terality_keys, client_bucket, client_key_prefix)
