# 重置索引
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83],
                  [12.4, 963, 0.73]],
                 index=['s1', 's2', 's3', 's4'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.reset_index())
