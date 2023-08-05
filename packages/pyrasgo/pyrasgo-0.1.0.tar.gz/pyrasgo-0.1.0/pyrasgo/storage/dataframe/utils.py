import pandas as pd
from typing import List, Optional

from pyrasgo.api.error import APIError
from pyrasgo.utils import naming


def build_schema(df: pd.DataFrame, include_index=False) -> dict:
    from pandas.io.json import build_table_schema
    schema_list = build_table_schema(df)
    if not include_index:
        return {column['name']: column
                for column in schema_list['fields'] if column['name'] != 'index'}
    return {column['name']: column
            for column in schema_list['fields']}


def generate_ddl(df: pd.DataFrame,
                 table_name: str,
                 append: Optional[bool] = False):
    #default is overwrite
    create_statement = "CREATE TABLE IF NOT EXISTS" if append else "CREATE OR REPLACE TABLE"
    return pd.io.sql.get_schema(df, table_name) \
        .replace("CREATE TABLE", create_statement) \
        .replace('"', '')

def confirm_df_columns(df: pd.DataFrame, dimensions: List[str], features: List[str]):
    confirm_list_columns(list(df.columns), dimensions, features)

def confirm_list_columns(columns: list, dimensions: List[str], features: List[str]):
    missing_dims = []
    missing_features = []
    consider = []
    for dim in dimensions:
        if dim not in columns:
            missing_dims.append(dim)
            if naming._snowflakify_name(dim) in columns:
                consider.append(naming._snowflakify_name(dim))
    for ft in features:
        if ft not in columns:
            missing_features.append(ft)
            if naming._snowflakify_name(ft) in columns:
                consider.append(naming._snowflakify_name(ft))
    if missing_dims or missing_features:
        raise APIError(f"Specified columns do not exist in dataframe: "
                        f"Dimensions({missing_dims}) Features({missing_features}) "
                        f"Consider these: ({consider})?")


def map_pandas_df_type(pandas_df_type: str) -> str:
    """For a given pandas dataframe type, return the equivalent python type.
    Default to input if no match"""
    if pandas_df_type.startswith('float'):
        return 'float'
    if pandas_df_type.startswith('datetime'):
        return 'datetime'
    if pandas_df_type.startswith('int'):
        return 'integer'
    return pandas_df_type


def _snowflakify_dataframe(df: pd.DataFrame):
    """
    Renames all columns in a pandas dataframe to Snowflake compliant names in place
    """
    df.rename(columns={r: naming._snowflakify_name(r) for r in build_schema(df)},
                inplace=True)