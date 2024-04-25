# 获取最大值/最小值
# 使用max()/min()可以获取列的最大值/最小值
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.max())  # 列最大值
print('*-*-*-*-*-')
print(a.min())  # 列最小值
