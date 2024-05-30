# 读取Excel文件
import pandas as pd

dat = pd.read_excel('read.xlsx', sheet_name='Sheet1')
print(dat)
print('-----')
print(dat.dtypes)
