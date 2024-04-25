# 根据行的前后值进行填充
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
print(a.fillna(method='bfill', axis=1))  # 行向后值填充
print('*-*-*-*-*-')
print(a.fillna(method='ffill', axis=1))  # 行向前值填充
