# 带有时间索引的数据框
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=pd.to_datetime(['2020-02-19', '2020-02-20', '2020-02-22']),
                 columns=['t', 'p', 'rh']
                 )
print(a)
