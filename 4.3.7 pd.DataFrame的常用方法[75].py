# 对时间戳类型的索引进行分组
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=pd.to_datetime(['2020-02-19', '2020-02-20', '2020-03-22']),
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.groupby(by=lambda x: x.month).sum())
