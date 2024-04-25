# 删除包含NaN的行或列
import numpy as np
import pandas as pd

a = pd.DataFrame([[np.nan, 983, 0.64],
                  [np.nan, np.nan, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('------')
b = a.dropna()  # 删除包含NaN的行
print(b)
print('-*-*-*-*-')
c = a.dropna(axis=1)  # 删除包含NaN的列
print(c)
