# 根据站号索引分组计算平均值
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2],
              index=['sta1', 'sta2', 'sta1', 'sta2'],
              name='t')
b = a.groupby(level=0).mean()
print(b)
