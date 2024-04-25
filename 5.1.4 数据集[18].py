# 使用assign()来修改或替换数据集的值
import xarray as xr
import pandas as pd
import numpy as np

temp = 15 + 8 * np.random.randn(2, 2, 3)
precip = 10 * np.random.rand(2, 2, 3)
lon = [[-99.83, -99.32], [-99.79, -99.23]]
lat = [[42.25, 42.21], [42.63, 42.59]]
ds = xr.Dataset()
ds["temperature"] = (("x", "y", "time"), temp)
ds["temperature_double"] = (("x", "y", "time"), temp * 2)
ds["precipitation"] = (("x", "y", "time"), precip)
ds.coords["lat"] = (("x", "y"), lat)
ds.coords["lon"] = (("x", "y"), lon)
ds.coords["time"] = pd.date_range("2014-09-06", periods=3)
ds.coords["reference_time"] = pd.Timestamp("2014-09-05")
print(ds)
ds.assign(temperature2=2 * ds.temperature)
print(ds)
