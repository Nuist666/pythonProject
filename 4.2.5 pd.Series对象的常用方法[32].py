# 按照索引排序
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=['b', 'd', 'c', 'a'],
              name='t')
print(a)
b = a.sort_index()
print(b)
c = a.sort_index(ascending=False)
print(c)
