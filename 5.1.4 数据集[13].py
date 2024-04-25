# 通过传递数据数组来创建数据集
import xarray as xr
import pandas as pd
import numpy as np

data = np.random.rand(4, 3)
locs = ["IA", "IL", "IN"]
times = pd.date_range("2000-01-01", periods=4)
foo = xr.DataArray(data, coords=[times, locs], dims=["time", "space"])
ds = xr.Dataset({"bar": foo})
print(ds)
