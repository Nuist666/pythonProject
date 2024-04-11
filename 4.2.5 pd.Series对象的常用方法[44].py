# 转换数据类型
import numpy as np
import pandas as pd

a = pd.Series([-9.5, 10.1, -11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
print(a)
b = a.astype(np.int32)
print(b)
