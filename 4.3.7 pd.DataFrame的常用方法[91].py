# 获取最大值/最小值对应的标签
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.idxmin())
print('*-*-*-*-*-')
print(a.idxmax())
print('~~~~~~')
print(a.idxmax(axis=1))
