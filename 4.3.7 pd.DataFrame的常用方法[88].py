# 按照数据排序
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.sort_values('p'))  # 按p列升序排列
print('*-*-*-*-*-')
print(a.sort_values('p', ascending=False))  # 按p列降序排列
