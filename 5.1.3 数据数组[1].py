# 快速创建数据数组
import xarray as xr
import numpy as np

data = np.random.rand(4, 3)
foo = xr.DataArray(data)
print(foo)
