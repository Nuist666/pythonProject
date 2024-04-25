# 以字典形式设置coords
import xarray as xr
import pandas as pd
import numpy as np

data = np.random.rand(4, 3)
times = pd.date_range("2000-01-01", periods=4)
locs = ["level", "latitude", "longitude"]
foo = xr.DataArray(data, coords={"time": times, "space": locs}, dims=["time", "space"])
print(foo)
