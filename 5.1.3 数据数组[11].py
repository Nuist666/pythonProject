# 使用rename()方法来修改DataArray的名字
import xarray as xr
import pandas as pd
import numpy as np

data = np.random.rand(4, 3)
times = pd.date_range("2000-01-01", periods=4)
locs = ["level", "latitude", "longitude"]
foo = xr.DataArray(data, coords={"time": times, "space": locs}, dims=["time", "space"])

foo_new = foo.rename("foo_new")
print(foo_new)
