# 获取最大值/最小值对应的位置
import numpy as np
import pandas as pd

a = pd.Series([9.5, np.nan, 11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
print(a.argmax())
print(a.argmin())
