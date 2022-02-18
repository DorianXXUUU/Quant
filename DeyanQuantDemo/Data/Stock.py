# pip install jqdatasdk


from jqdatasdk import *

auth('18888681090', 'Xudeyan0939')  # 账号是申请时所填写的手机号；密码为聚宽官网登录密码

# Shanghai .XSHG
# Shenzhen .XSHE
df = get_price('000001.XSHE', end_date='2021-02-22',
               count=100,
               frequency='daily',
               fields=['open', 'close', 'high', 'low', 'volume', 'money'])
print(df)
