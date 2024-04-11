# 根据阈值分组计算平均值
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=['a', 'b', 'c', 'd'],
              name='t')
b = a.groupby(a > 9.9).mean()
print(b)
