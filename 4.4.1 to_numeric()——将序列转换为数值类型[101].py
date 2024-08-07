# 将非数值类型的序列转换为数值类型
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  ['19.2', 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a.dtypes)
print('--------')
a['t'] = pd.to_numeric(a['t'])
print(a.dtypes)
