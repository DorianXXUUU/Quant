'''
@author: deyan
'''

import api.stock as st

code = '000001.XSHG'
# 调用一只股票的行情数据
data = st.get_single_price(code=code,
                           time_frequency='daily',
                           start_date='2021-02-01',
                           end_date='2021-03-01')

# 存入csv
st.export_date(data=data, filename=code, type='price')
