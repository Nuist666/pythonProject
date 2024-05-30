import xarray as xr
import numpy as np
import pandas as pd
from metpy.interpolate import inverse_distance_to_grid

df = pd.read_csv('r160.txt', sep='\s+', names=['lat', 'lon', 'pre_ano'])
lon = np.arange(76.0, 131.5+0.5, 0.5)
lat = np.arange(20.5, 51.5+0.5, 0.5)
lon_grid, lat_grid = np.meshgrid(lon, lat) # 生成交织的二维经纬栅格
# 注意：inverse_distance_to_grid()使用的目标栅格为交织后的二维经纬栅格
pre_grid = inverse_distance_to_grid(
              df['lon'].values,
              df['lat'].values,
              df['pre_ano'].values,
              lon_grid,
              lat_grid,
              r=15,
              min_neighbors=3
          )
pre_da = xr.DataArray(pre_grid, coords=[lat, lon], dims=['lat', 'lon'])

print(pre_da)

pre_grid1 = pre_da.interp(lon=[80, 90, 100, 120],
                      lat=[25, 30, 35, 40],
                      method='linear')
pre_sta = pre_da.interp(lon=lon, lat=lat, method='linear')
print(pre_sta)