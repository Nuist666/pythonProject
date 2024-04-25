# 使用类似字典的语法设置或删除坐标，如重新设置coords
import xarray as xr
import pandas as pd
import numpy as np

data = np.random.rand(4, 3)
times = pd.date_range("2000-01-01", periods=4)
locs = ["level", "latitude", "longitude"]
foo = xr.DataArray(data, coords={"time": times, "space": locs}, dims=["time", "space"])
foo["time"] = pd.date_range("1999-01-01", periods=4)
print(foo)
del foo["time"]
print(foo)
