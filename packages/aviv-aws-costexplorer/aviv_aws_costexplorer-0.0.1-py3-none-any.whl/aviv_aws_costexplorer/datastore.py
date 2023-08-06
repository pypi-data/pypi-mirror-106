import os
import logging
import pandas as pd
from . import costexplorer

BUCKET = os.environ.get("BUCKET")

# Read Data
def cau_read_athena(granularity: costexplorer.GranularityTypes='MONTHLY', dimension: str='RECORD_TYPE', where: str=None, tags: bool=False, **kwargs):
    if not 'wr' in globals():
        import awswrangler as wr
    query = f"SELECT * FROM {granularity.lower()} WHERE dimension='{dimension.upper()}' {'AND ' + where if where else ''}"
    if not tags:
        query += " AND tag IS NULL"
    logging.warning(query)
    return wr.athena.read_sql_query(query, database='cau', **kwargs)


def cau_read_parquet(granularity: costexplorer.GranularityTypes, basepath: str=BUCKET, **kwargs) -> dict:
    cau_path = f"{basepath}/cau/{granularity.lower()}"
    return read_parquet(path=cau_path, **kwargs)


def read_parquet(path: str, **kwargs) -> pd.DataFrame:
    if path.startswith('s3://'):
        if not 'wr' in globals():
            import awswrangler as wr
        kwargs['dataset'] = True
        return wr.s3.read_parquet(
            path=path,
            **kwargs
        )
    kwargs['engine'] = 'pyarrow'
    return pd.read_parquet(
        path=path,
        **kwargs
    )


# Write Data as parquet
def cau_to_parquet(data, basepath: str=BUCKET, **kwargs) -> dict:
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)
    if 'Granularity' not in data.columns:
        logging.error('CAU without Granularity!')
    granularity: str = data.Granularity[0].lower()
    data['AccountId'] = data.AccountId.astype('string')
    data['Start'] = pd.to_datetime(data['Start'])
    data['End'] = pd.to_datetime(data['End'])
    if granularity != 'hourly':
        data['Start'] = data['Start'].dt.date
        data['End'] = data['End'].dt.date

    data['Period'] = data.Start.astype('string')
    data['Period'] = data.Period.str.replace('-', '')
    if granularity == 'monthly':
        data['Period'] = data.Period.str[:-2]
    data['Period'] = data.Period.astype('int')

    if 'partition_cols' not in kwargs:
         kwargs['partition_cols'] = ['Period', 'AccountId']
    if 'mode' not in kwargs:
        kwargs['mode'] = 'overwrite_partitions'

    kwargs['database'] = 'cau'
    kwargs['table'] = granularity
    cau_path = f"{basepath}/cau/{granularity}"
    return to_parquet(data, path=cau_path, **kwargs)


def to_parquet(data, path: str, **kwargs) -> dict:
    """Do what it says and upload stuff to s3, with awswrangler help

    Args:
        data ([type]): Your data, ya' know
        path (str, optional): Base path for s3. Defaults to self.path (s3://FINOPS_BUCKET/FINOPS_DATA_VERSION/).
        partitions (list, optional): how awswrangler will partition data for s3.

    Returns:
        [type]: awswrangler obj
    """
    if not isinstance(data, pd.DataFrame):
        data = pd.DataFrame(data)

    if path.startswith('s3://'):
        if not 'wr' in globals():
            import awswrangler as wr
        kwargs['dataset'] = True
        # database MUST Exists in Glue
        # dbs = list(wr.catalog.databases()['Database'])
        # if 'database' in kwargs and kwargs['database'] not in dbs:
        #     wr.catalog.create_database(kwargs['database'])

        return wr.s3.to_parquet(
            df=data,
            path=path,
            **kwargs
        )

    for awsarg in ['database', 'table', 'mode']:
        if awsarg in kwargs:
            del kwargs[awsarg]
    kwargs['engine'] = 'pyarrow'
    return data.to_parquet(
        path=path,
        **kwargs
    )
