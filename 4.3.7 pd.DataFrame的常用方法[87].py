# 按照索引排序
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s2', 's1', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.sort_index())  # 升序排列
print('*-*-*-*-*-')
print(a.sort_index(ascending=False))  # 降序排列
