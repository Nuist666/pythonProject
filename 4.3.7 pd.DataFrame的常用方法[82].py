# 按照已有DataFrame对象的索引和列名排序
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
b = pd.DataFrame(data=None, index=['s2', 's1', 's3'], columns=['p', 't', 'rh'])
print(a)
print('--------')
print(a.reindex_like(b))
