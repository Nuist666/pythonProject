# 插值填充NaN
import numpy as np
import pandas as pd

a = pd.Series([8.0, np.nan, 10.0, 11.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
b = a.interpolate(method='linear')
print(b)
