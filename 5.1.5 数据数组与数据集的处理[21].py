# 创建数据数组
import xarray as xr
import pandas as pd
import numpy as np

da = xr.DataArray(np.random.rand(4, 3),
                  [("time", pd.date_range("2000-01-01", periods=4)), ("space", ["level", "lat", "lon"])])
print(da)
# 利用位置进行索引
print(da[0, 0])
print(da[:, [2, 1]])
# 使用.loc属性进行基于标签的索引
print(da.loc["2000-01-01":"2000-01-02", "lat"])
# 利用基于标签的索引来修改数据的值
da.loc["2000-01-01", ["lat", "lon"]] = -10
print(da)
# 利用维度名称进行索引
print(da[dict(space=0, time=slice(None, 2))])
# 利用维度坐标标签索引
print(da.loc[dict(time=slice("2000-01-01", "2000-01-02"))])
print(da.isel(space=0, time=slice(None, 2)))
print(da.sel(time=slice("2000-01-01", "2000-01-02")))
