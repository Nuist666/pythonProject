# 重命名序列
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=['a', 'b', 'c', 'd'],
              name='hello')
b = a.rename('t')
print(b)
