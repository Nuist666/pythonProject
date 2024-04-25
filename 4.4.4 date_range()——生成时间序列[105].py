# 生成时间序列
import pandas as pd

a = pd.date_range(start='2020-03-01', periods=3, freq='3H')
b = pd.date_range(start='2020-03-01', end='2020-03-03', freq='D')
c = pd.date_range(start='2020-03-01', end='2020-03-03')

print(a)
print(b)
print(c)
