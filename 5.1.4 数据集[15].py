# 访问数据集中的变量
import xarray as xr
import pandas as pd
import numpy as np

temp = 15 + 8 * np.random.randn(2, 2, 3)
precip = 10 * np.random.rand(2, 2, 3)
lon = [[-99.83, -99.32], [-99.79, -99.23]]
lat = [[42.25, 42.21], [42.63, 42.59]]
ds = xr.Dataset({"temperature": (["x", "y", "time"], temp),
                 "precipitation": (["x", "y", "time"], precip), },
                coords={"lon": (["x", "y"], lon),
                        "lat": (["x", "y"], lat),
                        "time": pd.date_range("2014-09-06", periods=3),
                        "reference_time": pd.Timestamp("2014-09-05")})
print(ds["temperature"])
