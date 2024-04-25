# 滑动窗口计算
# 对时间序列进行滑动计算
import pandas as pd

a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83],
                  [12.4, 963, 0.73]],
                 index=pd.to_datetime(['2020-02-19', '2020-02-20',
                                       '2020-02-21', '2020-02-22']),
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.rolling('2D').mean())
