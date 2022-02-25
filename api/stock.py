# pip install jqdatasdk
import datetime
import os
from jqdatasdk import *
import pandas as pd

# 设置行列不忽略
pd.set_option('display.max_row', 100000)
pd.set_option('display.max_columns', 1000)

auth('18888681090', 'Xudeyan0939')  # 账号是申请时所填写的手机号；密码为聚宽官网登录密码

# 全局变量
mac_root = '/Users/xudeyan/Desktop/Quant/api/data/'
windows_root = 'E:\\project\\Quant\\api\\data\\'


def get_stock_list():
    """
    获取所有A股股票列表
    :return stock_list
    """
    stocks = list(get_all_securities(['stock']).index)
    return stocks


def get_single_price(code, time_frequency, start_date, end_date):
    """
    获取单个股票行情数据
    :rtype: object
    :param code:
    :param time_frequency:
    :param start_date:
    :param end_date:
    :return:
    """
    data = get_price(code,
                     start_date=start_date,
                     end_date=end_date,
                     frequency=time_frequency)
    return data


def export_date(data, filename, type):
    """
    导出股票行情数据
    :param data:
    :param filename:
    :param type: price, finance
    :return:
    """

    # Mac/Linux directory
    file_root = mac_root + type + '/' + filename + '.csv'

    # Windows directory
    # file_root = windows_root + type + '\\' + filename + '.csv'
    if os.path.exists(file_root):
        data.to_csv(file_root, mode='a', header=False)
    else:
        # 判断一下file是否存在 > 存在：追加/不存在：保持不变
        data.to_csv(file_root)
    data.index.names = ['date']

    print("Saved Successful")


def get_csv_data(code, type):
    file_root = mac_root + type + '/' + code + '.csv'
    return pd.read_csv(file_root)


def transfer_price_freq(data, time_freq):
    """
    转换股票行情周期
    :param data:
    :param time_freq:
    :return:
    """
    df_trans = pd.DataFrame()
    df_trans['open'] = data['open'].resample(time_freq).first()
    df_trans['close'] = data['close'].resample(time_freq).last()
    df_trans['high'] = data['high'].resample(time_freq).max()
    df_trans['low'] = data['low'].resample(time_freq).min()

    return df_trans


def get_single_finance(code, date, statDate):
    """
    获取单个股票财务指标
    :param code:
    :param date:
    :param statDate:
    :return:
    """
    data = get_fundamentals(query(indicator).filter(indicator.code == code), date=date, statDate=statDate)
    return data


def get_single_valuation(code, date, statDate):
    """
    获取单个股票估值指标
    :param code:
    :param date:
    :param statDate:
    :return:
    """
    data = get_fundamentals(query(valuation).filter(valuation.code == code), date=date, statDate=statDate)
    return data
