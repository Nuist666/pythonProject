# 时间差的概念
import pandas as pd

a = pd.to_timedelta(['1 day', '10 min', '20S'])
b = pd.to_timedelta([1, 3, 5], unit='D')
print(a)
print(b)
