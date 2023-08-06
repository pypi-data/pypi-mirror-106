import json
from typing import Any, Callable, Dict, List

import numpy as np
import pandas as pd

from common_client_scheduler import (
    Display, ExportResponse, StructRef, IndexColNames, PandasIndexMetadata, PandasSeriesMetadata, PandasDFMetadata
)

from .. import Connection, DataTransfer, download_to_s3_files, AwsCredentialsFetcher


def _deserialize_display(aws_credentials: AwsCredentialsFetcher, to_display: Display):
    # No need to force it in package dependencies, if it gets called it means we are in a Jupyter Notebook
    # and and this dependency is present
    # noinspection PyUnresolvedReferences
    from IPython.display import display, HTML
    display(HTML(to_display.value))
    return None


def _deserialize_export(aws_credentials: AwsCredentialsFetcher, export: ExportResponse) -> None:
    path = export.path
    transfer_id = export.transfer_id
    if path.startswith('s3://'):
        download_to_s3_files(transfer_id, export.aws_region, path)
    else:
        DataTransfer.download_to_local_files(
            Connection.session.download_config, aws_credentials.get_credentials(), transfer_id, path, export.is_folder
        )


def _deserialize_np_array(aws_credentials: AwsCredentialsFetcher, value):
    # noinspection PyTypeChecker
    return np.load(DataTransfer.download_to_bytes(Connection.session.download_config, aws_credentials, value))


def _download_df(aws_credentials: AwsCredentialsFetcher, transfer_id: str, is_col_json: List[bool]) -> pd.DataFrame:
    df: pd.DataFrame = pd.read_parquet(  # type: ignore
        DataTransfer.download_to_bytes(
            Connection.session.download_config, aws_credentials.get_credentials(), transfer_id
        )
    )
    # Some data types require post-processing.
    for col_num in range(len(is_col_json)):
        if is_col_json[col_num]:
            df.iloc[:, col_num] = df.iloc[:, col_num].apply(json.loads)
    return df


def _rename_index(index: pd.Index, index_col_names: IndexColNames):
    if isinstance(index, pd.MultiIndex):
        index.names = index_col_names.names
    index.name = index_col_names.name


def _deserialize_index(aws_credentials: AwsCredentialsFetcher, index_metadata: PandasIndexMetadata) -> pd.Index:
    df = _download_df(aws_credentials, index_metadata.transfer_id, index_metadata.cols_json_encoded)
    if len(df.columns) == 1:
        index = pd.Index(data=df.iloc[:, 0])
    else:
        index = pd.MultiIndex.from_arrays([df.iloc[:, i] for i in range(len(df.columns))])
    _rename_index(index, index_metadata.index_col_names)
    return index


def _deserialize_series(aws_credentials: AwsCredentialsFetcher, series_metadata: PandasSeriesMetadata) -> pd.Series:
    df = _download_df(aws_credentials, series_metadata.transfer_id, series_metadata.cols_json_encoded)
    series = df.iloc[:, 0]
    series.name = series_metadata.series_name
    _rename_index(series.index, series_metadata.index_col_names)
    return series


def _deserialize_df(aws_credentials: AwsCredentialsFetcher, df_metadata: PandasDFMetadata) -> pd.DataFrame:
    df = _download_df(aws_credentials, df_metadata.transfer_id, df_metadata.cols_json_encoded)
    df.columns = df_metadata.col_names
    df.columns.name = df_metadata.col_names_name
    _rename_index(df.index, df_metadata.index_col_names)
    return df


_decoder: Dict[Any, Callable[[AwsCredentialsFetcher, Any], Any]] = {
    # np.ndarray: _deserialize_np_array,
    PandasIndexMetadata: _deserialize_index,
    PandasSeriesMetadata: _deserialize_series,
    PandasDFMetadata: _deserialize_df,
    Display: _deserialize_display,
    ExportResponse: _deserialize_export
}


def decode(credentials_fetcher: AwsCredentialsFetcher, o):
    from terality import Index, Series, DataFrame  # To avoid circular dependencies
    from terality._terality.terality_structures import DataFrameGroupBy
    structs = {
        'index': Index,
        'series': Series,
        'dataframe': DataFrame,
        'groupby_df': DataFrameGroupBy
    }

    if isinstance(o, StructRef):
        # noinspection PyProtectedMember
        return structs[o.type]._deser(id_=o.id)
    if type(o) in _decoder:
        return _decoder[type(o)](credentials_fetcher, o)
    return o
