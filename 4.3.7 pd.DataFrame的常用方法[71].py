# 仅删除全为NaN的行或列
import numpy as np
import pandas as pd

a = pd.DataFrame([[np.nan, 983, 0.64],
                  [np.nan, np.nan, np.nan],
                  [np.nan, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('------')
b = a.dropna(how='all')  # 删除全为NaN的行
print(b)
print('-*-*-*-*-')
c = a.dropna(axis=1, how='all')  # 删除全为NaN的列
print(c)
