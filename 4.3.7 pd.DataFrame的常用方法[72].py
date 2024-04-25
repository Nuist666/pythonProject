# 通过原始数据分组
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64, 'a'],
                  [19.2, 991, 0.75, 'b'],
                  [13.4, 973, 0.83, 'a'],
                  [13.4, 973, 0.83, 'b']],
                 index=['s1', 's2', 's3', 's2'],
                 columns=['t', 'p', 'rh', 'kind']
                 )
print(a)
print('--------')
print(a.groupby(level=0).sum())
print('-*-*-*-*-*')
print(a.groupby(level=0).size())
