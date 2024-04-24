# 按照时间索引条件提取
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=pd.to_datetime(['2020-02-19', '2020-02-20', '2020-02-22']),
                 columns=['t', 'p', 'rh']
                 )
b = a[a.index.day == 19]
print(b)
b = a[a.index.month == 2]
print(b)
b = a[a.index.year == 2020]
print(b)
