# 时间序列数据
import pandas as pd
import xarray as xr

print(pd.to_datetime(["2000-01-01", "2000-02-02"]))
print(pd.date_range("2000-01-01", periods=365))
import datetime

print(xr.Dataset({"time": datetime.datetime(2000, 1, 1)}))
