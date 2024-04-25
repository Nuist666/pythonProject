# 通过行、列标签或布尔序列访问多个元素
# 按标签访问行
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a.loc['s1'])  # Series
print('----------')
print(a.loc[['s1']])  # DataFrame
print('*-*-*-*-*-')
print(a.loc[['s1', 's3']])  # DataFrame
