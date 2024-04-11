# 升采样
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=pd.to_datetime(['2020-02-19', '2020-02-20',
                                    '2020-02-22', '2020-02-23']),
              name='t')
print(a.resample('1D').asfreq())
print(a.resample('1D').bfill())
