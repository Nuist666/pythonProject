# 删除缺测值NaN
import numpy as np
import pandas as pd

a = pd.Series([9.1, np.nan, 10.0, 11.2], index=['a', 'b', 'c', 'd'], name='t')
print(a)
b = a.dropna()
print(b)
