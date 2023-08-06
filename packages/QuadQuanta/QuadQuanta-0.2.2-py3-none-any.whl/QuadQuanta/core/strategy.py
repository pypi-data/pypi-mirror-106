#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   strategy.py
@Time    :   2021/05/14
@Author  :   levonwoo
@Version :   0.2
@Contact :   
@License :   (C)Copyright 2020-2021
@Desc    :   None
'''

# here put the import lib
import numpy as np

from QuadQuanta.data import query_clickhouse


class BaseStrategy():
    """
    策略基类
    """
    def __init__(self,
                 code=None,
                 start_date=None,
                 end_date=None,
                 frequency='day'):
        self.start_date = start_date
        self.end_date = end_date
        self.frequency = frequency
        # 初始化时加载日线数据
        self.day_data = query_clickhouse(code, start_date, end_date, 'day')
        self.subscribe_code = np.unique(self.day_data['code']).tolist()
        self.trading_date = np.sort(np.unique(self.day_data['date']))
        self.trading_datetime = np.sort(np.unique(self.day_data['datetime']))

    def init(self):
        """
        策略初始化
        """
        raise NotImplementedError

    def on_bar(self, bar):
        """
        
        """
        raise NotImplementedError

    def on_tick(self, tick):
        raise NotImplementedError

    def syn_backtest(self):
        raise NotImplementedError

    # TODO
    async def asyn_backtest(self):
        """
        异步回测
        """
        raise NotImplementedError


if __name__ == '__main__':
    strategy = BaseStrategy(start_date='2014-01-01',
                            end_date='2014-01-10',
                            frequency='min')
    strategy.syn_backtest()
