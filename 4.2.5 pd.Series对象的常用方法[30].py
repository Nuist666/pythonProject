# 中央平均的滑动窗口计算
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2, 12.1, 13.6, 14.5, 10.1],
              name='t')
b = a.rolling(3, center=True).mean()
print(b)
