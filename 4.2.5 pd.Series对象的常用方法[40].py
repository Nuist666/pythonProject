# 计算绝对值
import pandas as pd

a = pd.Series([-9.5, 10.1, -11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
print(a.abs())
