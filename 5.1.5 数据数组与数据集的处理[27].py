# 通过设置skipna=False来禁止跳过缺测值NaN
import xarray as xr
import numpy as np

print(xr.DataArray([1, 2, np.nan, 3]).mean())
print(xr.DataArray([1, 2, np.nan, 3]).mean(skipna=False))
