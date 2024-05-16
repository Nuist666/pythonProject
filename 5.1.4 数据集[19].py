# 使用assign_coords()对DataArray的坐标标签进行重新声明
import xarray as xr
import numpy as np

da = xr.DataArray(np.random.rand(4), coords=[np.array([358, 359, 0, 1])], dims="lon")
print(da)
da.assign_coords(lon=(((da.lon + 180) % 360) - 180))
print(da)
