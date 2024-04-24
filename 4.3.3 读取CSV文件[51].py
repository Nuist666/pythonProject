# 以其他列为索引
import pandas as pd

a = pd.read_csv('pandas_read.csv', index_col=2)
print(a)
