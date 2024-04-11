# 转换为列表对象
import pandas as pd

a = pd.Series([-9.5, 10.1, -11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
b = a.to_list()
print(b)
print(type(b))
