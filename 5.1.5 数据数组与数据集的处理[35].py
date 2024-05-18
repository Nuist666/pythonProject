# 沿多个维度组合数据集或数据数组
import xarray as xr

arr = xr.DataArray(name="temperature", data=[[1, 2], [3, 4]], dims=["x", "y"])
ds_grid = [[arr, arr], [arr, arr]]
print(xr.combine_nested(ds_grid, concat_dim=["x", "y"]))
# 从数据的坐标自动推断顺序
x1 = xr.DataArray(name="foo", data=[1, 2, 3], coords=[("x", [1, 2, 3])])
x2 = xr.DataArray(name="foo", data=[4, 5, 6], coords=[("x", [4, 5, 6])])
print(xr.combine_by_coords([x2, x1]))
