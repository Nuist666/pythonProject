import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import cartopy.mpl.ticker as cticker

#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
u = f['uwnd'].loc['2005-07-01', 500, :, :].values
v = f['vwnd'].loc['2005-07-01', 500, :, :].values
lat = f['lat']
lon = f['lon']
#创建Figure
fig = plt.figure(figsize=(16, 13))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.Mercator())
#设置ax1的范围
ax1.set_extent([80, 140, 0, 40])
#为ax1添加海岸线
ax1.coastlines()
#为ax1添加地理经纬度标签及刻度
ax1.set_xticks(np.arange(80, 160, 20), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(0, 60, 20), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#绘制500hPa水平风场
q1 = ax1.quiver(lon, lat, u, v, scale=200, transform=ccrs.PlateCarree())
#添加参考矢量
ax1.quiverkey(q1, 0.9, 1.01, U=30, label='30m/s')
#添加图题
ax1.set_title('(a) July 2005 500hPa UV', loc='center', fontsize=18)
#绘制ax2
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.Mercator())
#设置ax2的范围
ax2.set_extent([80, 140, 0, 40])
#为ax2添加海岸线
ax2.coastlines()
#为ax2添加地理经纬度标签及刻度
ax2.set_xticks(np.arange(80, 160, 20), crs=ccrs.PlateCarree())
ax2.set_yticks(np.arange(0, 60, 20), crs=ccrs.PlateCarree())
ax2.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax2.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#绘制500hPa水平风场，[::2,::2]表示每隔两个栅格绘制一次，避免箭头过于密集
q1 = ax2.quiver(lon[::2], lat[::2], u[::2, ::2], v[::2, ::2], scale=200, transform=ccrs.PlateCarree())
#添加参考矢量
ax1.quiverkey(q1, 0.9, 1.01, U=30, label='30m/s')
#添加图题
ax2.set_title('(b) July 2005 500hPa UV', loc='center', fontsize=18)
plt.show()
