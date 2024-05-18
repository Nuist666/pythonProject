# 数据的移动和滚动
import xarray as xr

array = xr.DataArray([1, 2, 3, 4], dims="x")
print(array)
# 将数据向右侧移动两次
print(array.shift(x=2))
# 将数据向右滚动两次
print(array.roll(x=2, roll_coords=True))
