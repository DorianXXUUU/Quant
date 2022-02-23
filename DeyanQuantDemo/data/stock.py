# pip install jqdatasdk
import datetime

from jqdatasdk import *
import pandas as pd
import datetime

# 设置行列不忽略
pd.set_option('display.max_row', 100000)
pd.set_option('display.max_columns', 1000)

auth('18888681090', 'Xudeyan0939')  # 账号是申请时所填写的手机号；密码为聚宽官网登录密码
#
# # Shanghai .XSHG
# # Shenzhen .XSHE
#
# # print(df)
# # 获取所有A股
#
# # stocks = list(get_all_securities(['stock']).index)
# # # print(stocks)
# #
# # df = get_price(stocks, end_date='2022-02-18',
# #                count=10,
# #                frequency='daily',
# #                fields=['open', 'close', 'high', 'low', 'volume', 'money'])
# # print(df)
#
# # resample函数的使用
# # 转换周期：日K to 周K
# # 获取日K
# df = get_price('000001.XSHG', end_date='2021-02-22',
#                count=20,
#                frequency='daily',
#                fields=['open', 'close', 'high', 'low', 'volume', 'money'])
#
# df['weekday'] = df.index.weekday
# print(df)
# # 获取周K：当周的开盘价 收盘价 最高价 最低价
# df_week = pd.DataFrame()
# df_week['open'] = df['open'].resample('W').first()
# df_week['close'] = df['close'].resample('W').last()
# df_week['high'] = df['high'].resample('W').max()
# df_week['low'] = df['low'].resample('W').min()
#
# # 汇总统计：统计一下月成交量、成交额（sum）
# df_week['volume(sum)'] = df['volume'].resample('W').sum()
# df_week['money(sum)'] = df['money'].resample('W').sum()

# print(df_week)

'''获取股票财务指标'''
df = get_fundamentals(query(indicator), statDate='2020')
# print(df)
# 存储数据
# df.to_csv('/Users/xudeyan/desktop/Quant/DeyanQuantDemo/data/finance/finance2020.csv')

# 基于盈利指标选股：e ps，operating_profit, roe, inc_net_profit_year_on_year
#
# df = df[(df['eps'] > 0) &
#         (df['operating_profit'] > 3000000000) &
#         (df['roe'] > 11) &
#         (df['inc_net_profit_year_on_year'] > 10)]
df = df[(df['eps'] > 0) &
        (df['roe'] > 11) &
        (df['inc_net_profit_year_on_year'] > 10)]

df.index = df['code']
# print(df.head())

'''获取股票估值指标'''
df_valuation = get_fundamentals(query(valuation), date='2021-2-22')
df_valuation.index = df_valuation['code']

df['pe_ratio'] = df_valuation['pe_ratio']
df = df[df['pe_ratio'] < 50]
# print(df_valuation.head())
print(df.head(n=10))