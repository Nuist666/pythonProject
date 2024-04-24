# 读取带有时间列的CSV文件
import pandas as pd

a = pd.read_csv('pandas_read_date.csv', parse_dates=[0])
print(a)
print('----------')
print(a.dtypes)
# 直接指定time列为索引
import pandas as pd

a = pd.read_csv('pandas_read_date.csv', parse_dates=[0], index_col=0)
print(a)
# 当时间列为多列时
import pandas as pd

a = pd.read_csv('pandas_read_datetime.csv',
                parse_dates=[[0, 1]],
                index_col=0)
print(a)
