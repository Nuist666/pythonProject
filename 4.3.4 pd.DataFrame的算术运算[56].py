# pd.DataFrame与pd.Series的算术运算
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
b = pd.Series([10, -100, 0], index=['p', 't', 'rh'])
print(a + b)
