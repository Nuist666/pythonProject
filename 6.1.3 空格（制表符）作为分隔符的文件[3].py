# 读取空格为分隔符的文件
import numpy as np
import pandas as pd

dat = pd.read_csv('sta.txt',
                  sep='\s+',  # 如果是空格分隔符，则此处参数值为1s
                  parse_dates=['time'],
                  date_format='%Y-%m-%d %H:%M:%S',  # 指定日期格式
                  dtype={'station': np.unicode_})

print(dat.dtypes)
print('--------')
print(dat)
