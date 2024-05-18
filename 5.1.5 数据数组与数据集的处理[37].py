# datetime索引
import pandas as pd
import xarray as xr
import numpy as np
import datetime

time = pd.date_range("2000-01-01", freq="H", periods=365 * 24)
ds = xr.Dataset({"foo": ("time", np.arange(365 * 24)), "time": time})
print(ds.sel(time="2000-01"))
print(ds.sel(time=slice("2000-06-01", "2000-06-10")))
print(ds.sel(time=datetime.time(12)))
