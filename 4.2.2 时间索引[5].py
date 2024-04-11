# 时区转换
import datetime as dt
import pandas as pd

index_time = pd.to_datetime(['2020-02-19', '2020-02-20', '2020-02-21', '2020-02-22'])
index_time = index_time - dt.timedelta(hours=8)
a = pd.Series([9.1, 9.5, 10.0, 11.2], index=index_time, name='t')
print(a)
