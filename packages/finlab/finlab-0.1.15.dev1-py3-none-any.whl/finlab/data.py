import requests
import datetime
import pandas as pd
from io import BytesIO
from . import get_token
from . import dataframe
import numpy as np

cache = {}
cache_time = {}
stock_names = {}


def get(dataset, use_cache=True):
    global stock_names

    # use cache if possible
    now = datetime.datetime.now()
    if (use_cache and (dataset in cache) and
            (now - cache_time[dataset] < datetime.timedelta(days=1))):
        return cache[dataset]

    api_token = get_token()

    if ':' in dataset:
        bucket_name = 'finlab_tw_stock_item'
        blob_name = dataset.replace(':', '#') + '.feather'
        file_format = 'pivot'
    else:
        bucket_name = 'finlab_tw_stock'
        blob_name = dataset + '.feather'
        file_format = 'table'

    # request for auth url
    request_args = {
        'api_token': api_token,
        'bucket_name': bucket_name,
        'blob_name': blob_name
    }

    url = 'https://asia-east2-fdata-299302.cloudfunctions.net/auth_generate_data_url'
    auth_url = requests.get(url, request_args)

    # download and parse dataframe
    res = requests.get(auth_url.text)
    df = pd.read_feather(BytesIO(res.content))

    # set date as index
    if file_format == 'pivot':
        df.set_index('date', inplace=True)

        # if column is stock name
        if (df.columns.str.find(' ') != -1).all():
            # save new stock names
            new_stock_names = df.columns.str.split(' ')
            new_stock_names = dict(zip(new_stock_names.str[0], new_stock_names.str[1]))
            stock_names = {**stock_names, **new_stock_names}

            # remove stock names
            df.columns = df.columns.str.split(' ').str[0]

            # combine same stock history according to sid
            df = df.transpose().groupby(level=0).mean().transpose()

        df = dataframe.FinlabDataFrame(df)

    # save cache
    if use_cache:
        cache[dataset] = df
        cache_time[dataset] = now

    return df


def get_adj(price_option='收盤價'):
    def adj_holiday(item, df):
        all_index = (df.index | item.index).sort_values()
        all_index = all_index[all_index >= item.index[0]]

        df = df.reindex(all_index)
        group = all_index.isin(item.index).cumsum()
        df = df.groupby(group).mean()
        df.index = item.index
        return df

    item = get(f'price:{price_option}')
    ratio1 = adj_holiday(item, get('capital_reduction_otc:otc_cap_divide_ratio'))
    ratio2 = adj_holiday(item, get('capital_reduction_tse:twse_cap_divide_ratio'))
    ratio3 = adj_holiday(item, get('dividend_otc:otc_divide_ratio'))
    ratio4 = adj_holiday(item, get('dividend_tse:twse_divide_ratio'))

    divide_ratio = (ratio1.reindex_like(item).fillna(1)
                    * ratio2.reindex_like(item).fillna(1)
                    * ratio3.reindex_like(item).fillna(1)
                    * ratio4.reindex_like(item).fillna(1)).cumprod()

    divide_ratio[np.isinf(divide_ratio)] = 1
    return item * divide_ratio
