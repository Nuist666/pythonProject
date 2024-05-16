# 保持数据的原始形状，且需要掩盖掉某些元素
import xarray as xr
import numpy as np

da = xr.DataArray(np.arange(16).reshape(4, 4), dims=["x", "y"])
print(da.where(da.y < 2))
# 剔除缺测部分
print(da.where(da.y < 2, drop=True))
