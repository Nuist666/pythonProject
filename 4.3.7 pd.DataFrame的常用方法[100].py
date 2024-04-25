# 转换数据类型
# 指定列转换
import numpy as np
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a.dtypes)
print('--------')
b = a.astype({'t': np.float32, 'p': np.float64})
print(b.dtypes)
