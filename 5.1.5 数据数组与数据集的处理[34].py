# 数据合并
import xarray as xr
import numpy as np

arr = xr.DataArray(np.random.randn(2, 3), [("x", ["a", "b"]), ("y", [10, 20, 30])])
print(arr)
# 合并数据数组arr的两个子数组
print(xr.concat([arr[:, 2:], arr[:, 1:]], dim="y"))
# 使用不同变量组合数据集或数据数组
print(xr.merge([xr.DataArray(n, name="var%d" % n) for n in range(5)]))
# 使用不同索引或缺失值组合数据集或数据数组
ar0 = xr.DataArray([[0, 0], [0, 0]], [("x", ["a", "b"]), ("y", [-1, 0])])
ar1 = xr.DataArray([[1, 1], [1, 1]], [("x", ["b", "c"]), ("y", [0, 1])])
print(ar0.combine_first(ar1))
print(ar1.combine_first(ar0))
