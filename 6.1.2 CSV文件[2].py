# 将站号指定为字符串类型
import numpy as np
import pandas as pd

dat = pd.read_csv('sta.csv',
                  parse_dates=['time'],
                  dtype={'station': np.unicode_})
print(dat.dtypes)
print('--------')
print(dat)
