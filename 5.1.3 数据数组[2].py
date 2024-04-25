# 创建完整数据数组
import xarray as xr
import numpy as np
import pandas as pd

data = np.random.rand(4, 3)
locs = ["level", "latitude", "longitude"]
times = pd.date_range("2000-01-01", periods=4)
foo = xr.DataArray(data, coords=[times, locs], dims=["time", "space"])
print(foo)
