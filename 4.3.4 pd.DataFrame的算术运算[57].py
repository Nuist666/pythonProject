# pd.DataFrame与pd.DataFrame的算术运算
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
b = pd.DataFrame([[20, -14, -0.25],
                  [10, -5, -0.14],
                  [17, -3, -0.33]],
                 index=['s2', 's1', 's3'],
                 columns=['p', 't', 'rh']
                 )
print(a + b)
