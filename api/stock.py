# pip install jqdatasdk
import datetime

from jqdatasdk import *
import pandas as pd
import datetime

# 设置行列不忽略
pd.set_option('display.max_row', 100000)
pd.set_option('display.max_columns', 1000)

auth('18888681090', 'Xudeyan0939')  # 账号是申请时所填写的手机号；密码为聚宽官网登录密码


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
    # file_root = '/Users/xudeyan/Desktop/Quant/api/data/' + type + '/' + filename + '.csv'

    # Windows directory
    file_root = 'E:\\project\\Quant\\api\\data\\' + type + '\\' + filename + '.csv'
    data.to_csv(file_root)
    print("Saved Successful")


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


