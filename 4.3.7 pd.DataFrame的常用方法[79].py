# 用指定值填充或根据行或列的前后值填充
import numpy as np
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, np.nan, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.fillna(9999))  # 用值填充
print('*-*-*-*-*-')
print(a.fillna(method='bfill'))  # 列向后值填充
print('**********')
print(a.fillna(method='ffill'))  # 列向前值填充
