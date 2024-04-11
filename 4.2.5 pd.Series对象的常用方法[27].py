# 使用reindex_like()可以用一个序列的索引来对另一个序列进行排序
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=['a', 'b', 'c', 'd'],
              name='t1')
b = pd.Series([0, 0, 0, 0],
              index=['b', 'd', 'a', 'd'],
              name='t2')
print(a)
c = a.reindex_like(b)
print(c)
