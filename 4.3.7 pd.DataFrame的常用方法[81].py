# 按照指定序列/索引和列名排序
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.reindex(['s2', 's3', 's1']))
print('*-*-*-*-*-')
print(a.reindex(index=['s2', 's3', 's1'], columns=['rh', 't', 'p']))
