'''
用来创建交易策略、生成交易信号
'''

import api.stock as st
import numpy as np
import pandas as pd


def week_period_strategy(code, time_frequency, start_date, end_date):
    data = st.get_single_price(code, time_frequency, start_date, end_date)
    # 新建周期字段
    data['weekday'] = data.index.weekday
    # 周四交易：买入
    data['buy_signal'] = np.where((data['weekday'] == 3), 1, 0)
    # 周一交易：卖出
    data['sell_signal'] = np.where((data['weekday'] == 0), -1, 0)

    return data


if __name__ == '__main__':
    data = week_period_strategy('000001.XSHE', 'daily', '2020-01-01', '2020-03-01')
    print(data[['close', 'weekday', 'buy_signal', 'sell_signal']])
