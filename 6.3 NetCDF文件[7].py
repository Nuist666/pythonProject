# 读取NetCDF文件
import xarray as xr

# 将文件路径改为自己的
dataset = xr.open_dataset('1980060106.nc')
print(dataset)
t = dataset['t']
print(t)
