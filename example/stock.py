'''
@author: deyan
@desc: 获取价格， 计算涨跌幅
'''

import api.stock as st

# 获取平安银行的行情数据 日K
data = st.get_single_price(code='000001.XSHE',
                           time_frequency='daily',
                           start_date='2020-01-01',
                           end_date='2020-02-01'
                           )
# print(data)
# 计算涨跌幅，验证准确性
data = st.calculate_change_pct(data)
# print(data)

# 获取周K
data = st.transfer_price_freq(data, 'W')
print(data)

# 计算涨跌幅
data = st.calculate_change_pct(data)
print(data)