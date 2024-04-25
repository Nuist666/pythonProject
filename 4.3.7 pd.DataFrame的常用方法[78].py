# 填充NaN
# 通过插值的方式填充
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
print(a.interpolate(method='linear'))  # 列向线性插值
print('*-*-*-*-*-')
print(a.interpolate(method='linear', axis=1))  # 行向线性插值
