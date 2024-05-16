# 聚合运算
import xarray as xr
import numpy as np

arr = xr.DataArray(np.random.RandomState(0).randn(2, 3), [("lat", [5, 10]), ("lon", [15, 20, 25])])
print(arr)
# 对其沿lat轴求和
print(arr.sum(dim="lat"))
# 对整个数据数组求标准差
print(arr.std(["lat", "lon"]))
# 返回整个数据数组的最小值
print(arr.min())
