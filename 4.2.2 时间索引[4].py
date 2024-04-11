# 为时间序列准备的统计计算方法
import pandas as pd
import numpy as np

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=pd.to_datetime(['2020-02-19', '2020-02-20',
                                    '2020-02-21', '2020-02-22']),
              name='t')
print(a)
print(a.index.astype(np.int64))
