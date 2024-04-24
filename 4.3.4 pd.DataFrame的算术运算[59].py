# 按多个数据条件提取满足条件的行
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
b = a[(a['t'] < 20) & (a['rh'] > 0.8)]
print(b)
b = a[(a['t'] < 19) | (a['rh'] < 0.7)]
print(b)
