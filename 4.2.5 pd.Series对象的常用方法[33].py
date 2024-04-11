# 按照数据排序
import pandas as pd

a = pd.Series([9.5, 9.1, 11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
print(a)
b = a.sort_values()
print(b)
c = a.sort_values(ascending=False)
print(c)
