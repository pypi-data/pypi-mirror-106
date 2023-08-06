#-*-coding:utf-8-*-
# 历史代码文件，保存优化前的代码
import datetime
import jqdatasdk as jq
# from jqdatasdk import normalize_code, get_price, get_all_securities
from clickhouse_driver import Client
from QuadQuanta.utils.datetime_func import date_convert_stamp
from collections import OrderedDict
from clickhouse_api import create_clickhouse_table, insert_to_clickhouse, query_exist_max_datetime, \
    create_clickhouse_database


def fetch_single_jqdata(code: str, start_time: str, end_time: str, client,
                        frequency: str):
    """
    获取起止时间内单个聚宽股票并添加自定义字段

    Parameters
    ----------
    code : str
        [description]
    start_time : str
        [description]
    end_time : str
        [description]
    client : [type]
        [description]
    frequency : str
        [description]

    Returns
    -------
    [type]
        [description]
    """
    print(code)
    # 查询最大datetime
    exist_max_datetime = query_exist_max_datetime(code, frequency, client)[0][0]
    # 数据从2014年开始保存 TODO 可从yaml文件更改数据起始点
    if str(exist_max_datetime) > '2014-01-01':
        _start_time = str(exist_max_datetime + datetime.timedelta(hours=18))
    else:
        if start_time < '2014-01-01':
            start_time = '2014-01-01' + ' 9:00:00'
        _start_time = start_time

    if _start_time < end_time:
        pd_data = jq.get_price(jq.normalize_code(code),
                               start_date=_start_time,
                               end_date=end_time,
                               frequency=frequency,
                               fields=[
                                   'open', 'close', 'high', 'low', 'volume',
                                   'money', 'avg', 'high_limit', 'low_limit',
                                   'pre_close'
                               ],
                               skip_paused=True,
                               fq='none',
                               count=None,
                               panel=False).dropna(axis=0,
                                                   how='any')  # 删除包含NAN的行
    else:
        return None

    pd_data['datetime'] = pd_data.index
    pd_data['code'] = code
    pd_data['amount'] = pd_data['money']
    return pd_data.assign(
        date=pd_data['datetime'].apply(lambda x: str(x)[0:10]),
        date_stamp=pd_data['datetime'].apply(
            lambda x: date_convert_stamp(x))).set_index('datetime',
                                                        drop=True,
                                                        inplace=False)


def fetch_multi_jqdata(code: list, start_time: str, end_time: str, client,
                       frequency: str):
    """
    获取起止时间内多个聚宽股票并添加自定义字段

    Parameters
    ----------
    code : list
        [description]
    start_time : str
        [description]
    end_time : str
        [description]
    client : [type]
        [description]
    frequency : str
        [description]

    Returns
    -------
    [type]
        [description]
    """
    if isinstance(code, str):
        code = list(map(str.strip, code.split(',')))
    if len(code) < 2:
        return fetch_single_jqdata(str(code), start_time, end_time, client,
                                   frequency)
    # 查询最大datetime
    exist_max_datetime = query_exist_max_datetime(code, frequency, client)[0][0]
    # 数据从2014年开始保存 TODO 可从yaml文件更改数据起始点
    if str(exist_max_datetime) > '2014-01-01':
        _start_time = str(exist_max_datetime + datetime.timedelta(hours=18))
    else:
        if start_time < '2014-01-01':
            start_time = '2014-01-01' + ' 9:00:00'
        _start_time = start_time

    if _start_time < end_time:
        pd_data = jq.get_price(jq.normalize_code(code),
                               start_date=_start_time,
                               end_date=end_time,
                               frequency=frequency,
                               fields=[
                                   'open', 'close', 'high', 'low', 'volume',
                                   'money', 'avg', 'high_limit', 'low_limit',
                                   'pre_close'
                               ],
                               skip_paused=True,
                               fq='none',
                               count=None,
                               panel=False).dropna(axis=0,
                                                   how='any')  # 删除包含NAN的行
    else:
        return None

    pd_data['datetime'] = pd_data['time']
    pd_data['code'] = pd_data['code']
    pd_data['amount'] = pd_data['money']
    return pd_data.assign(
        date=pd_data['datetime'].apply(lambda x: str(x)[0:10]),
        date_stamp=pd_data['datetime'].apply(
            lambda x: date_convert_stamp(x))).set_index('datetime',
                                                        drop=True,
                                                        inplace=False)


if __name__ == '__main__':
    pass