# 序列的数据维度
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2], index=['a', 'b', 'c', 'd'], name='t')
print(a.ndim)
