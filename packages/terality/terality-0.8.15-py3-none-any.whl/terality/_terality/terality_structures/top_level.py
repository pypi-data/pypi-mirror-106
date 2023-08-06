from functools import partial
from uuid import uuid4

import pandas as pd

from common_client_scheduler import UploadRequest
from terality._terality import Connection, AwsCredentialsFetcher

from .. import upload_local_files, upload_s3_files
from . import call_pandas_function


def make_upload(path: str) -> UploadRequest:
    if path.startswith('s3://'):
        parts = path[len("s3://"):].split("/", 1)
        if len(parts) != 2:
            raise ValueError(f"Invalid S3 path, expected format: 's3://bucket/prefix' (prefix may be the empty string), got: '{path}'.")
        transfer_id = upload_s3_files(s3_bucket=parts[0], s3_key_prefix=parts[1])
        aws_region = Connection.session.upload_config.default_aws_region
    else:
        transfer_id = str(uuid4())
        credentials_fetcher = AwsCredentialsFetcher()
        upload_local_files(path, transfer_id, credentials_fetcher.get_credentials())
        aws_region = None
    return UploadRequest(transfer_id=transfer_id, aws_region=aws_region)


def _treat_read_job(method_name, *args, **kwargs):
    """ Special job to intercept file arguments and upload them to Terality for pd.read_xxx() jobs"""
    if 'path' in kwargs:
        kwargs['path'] = make_upload(kwargs['path'])
    else:
        path, *others = args
        args = [make_upload(path)] + others
    return call_pandas_function('free_function', None, method_name, *args, **kwargs)


_read_top_level_functions = {'read_parquet', 'read_csv'}


_top_level_functions = _read_top_level_functions | set()


def _get_top_level_attribute(attribute: str):
    if callable(pd.__getattribute__(attribute)):
        if attribute in _read_top_level_functions:
            return partial(_treat_read_job, attribute)
        return partial(call_pandas_function, 'free_function', None, attribute)
    raise AttributeError(f'Name {attribute!r} is not defined')
