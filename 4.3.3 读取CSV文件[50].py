# 读取带有索引和列名的CSV文件
import pandas as pd

a = pd.read_csv('pandas_read.csv', index_col=0)
print(a)
