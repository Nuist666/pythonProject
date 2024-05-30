# 读取栅格型文本数据
# 行列与经纬栅格相关
import numpy as np
import xarray as xr

array_raw = np.loadtxt('grid_1.txt', dtype=np.float64)
print(array_raw)  # 这一行用于演示读取结果，并非必要输入， 数据量过大时可能会导致卡顿
lon = np.linspace(120, 122.5, 5)
lat = np.linspace(10, 13, 4)
print(lon)  # 此行仅用于演示
print(lat)  # 此行仅用于演示
t_grid = xr.DataArray(array_raw, coords=[lat, lon], dims=["lat", "lon"])
print(t_grid)
