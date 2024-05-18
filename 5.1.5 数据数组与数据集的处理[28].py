# 数据滑动
import xarray as xr
import numpy as np

arr = xr.DataArray(np.arange(0, 7.5, 0.5).reshape(3, 5), dims=("lat", "lon"))
print(arr)
print(arr.rolling(lon=3))
# 聚合运算的方法可以直接对Rolling对象使用
r = arr.rolling(lon=3)
print(r.mean())
# 通过传递center=True来使结果居中
r = arr.rolling(lon=3, center=True)
print(r.mean())
# 在调用 rolling()时设置min_periods将更改窗口中的最小滑动长度，以便在聚合时具有值
r = arr.rolling(lon=3, center=True, min_periods=2)
print(r.mean())
# 多维度滑动
print(arr.rolling(lat=2, lon=3, min_periods=2))
