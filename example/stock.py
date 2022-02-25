'''
@author: deyan
'''

import api.stock as st
import time
from apscheduler.schedulers.blocking import BlockingScheduler
import logging
import pandas as pd

LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
logging.basicConfig(filename='mypython.log', level=logging.INFO, format=LOG_FORMAT)
code = '000001.XSHE'

data = st.get_single_price(code=code,
                           time_frequency='daily',
                           start_date='2021-02-26',
                           end_date='2021-03-15')

#
# 存入csv
st.export_date(data=data, filename=code, type='price')

# 从csv中获取数据
data = st.get_csv_data(code=code, type='price')
print(data)


def append_everyday_data():
    """
    实时更新数据 假设每天更新 > 存到csv文件里 > data.to_csv(append)
    :return:
    """
    date_time = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    data_realtime = st.get_single_price(code=code,
                                        time_frequency='daily',
                                        start_date=date_time,
                                        end_date=date_time)
    st.export_date(data=data_realtime, filename=code, type='price')

#
# if __name__ == "__main__":
#     scheduler = BlockingScheduler()
#     scheduler.add_job(append_everyday_data, 'cron', day='1-31', hour=17)
#     scheduler.start()
