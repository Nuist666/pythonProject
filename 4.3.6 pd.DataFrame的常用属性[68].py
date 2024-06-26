# 通过行、列位置访问多个元素
# 按位置访问列
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a.iloc[:, 0])  # Series
print('----------')
print(a.iloc[:, [0]])  # DataFrame
print('*-*-*-*-*-')
print(a.iloc[:, [0, 2]])  # DataFrame
