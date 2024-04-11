# 按规则映射元素
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=['a', 'b', 'c', 'd'],
              name='t')
b = a.map(lambda x: x - 5)
print(b)
