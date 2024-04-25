# 计算标准差/无偏方差
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.std())  # 按列计算标准差
print('*-*-*-*-*-')
print(a.var())  # 按列计算无偏方差
print('~~~~~~')
print(a.std(axis=1))
