# 计算协方差
import pandas as pd

a = pd.Series([9.5, 10.1, 11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t1')
b = pd.Series([8.5, 9.1, 12.1, 10.5],
              index=['a', 'b', 'c', 'd'],
              name='t2')
print(a.cov(b))
