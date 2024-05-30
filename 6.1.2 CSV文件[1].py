# 读取csv，同时将时间字符串解析为时间戳类型
import pandas as pd

dat = pd.read_csv('sta.csv', parse_dates=['time'])
print(dat.dtypes)
print('--------')
print(dat)
