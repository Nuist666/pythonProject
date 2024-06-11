import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
u = f['uwnd'].loc['2005-07-01',500,:,:].values
v = f['vwnd'].loc['2005-07-01',500,:,:].values
lat = f['lat']
lon = f['lon']
#创建Figure
fig = plt.figure(figsize=(16, 13))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(1,1,1, projection=ccrs.PlateCarree())
#设置ax1的范围
ax1.set_extent([80,140,0,40])
#为ax1添加海岸线
#ax1.coastlines()
#为ax1添加地理经纬度标签及刻度
ax1.set_xticks(np.arange(80,160,20), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(0,60,20), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#绘制500hPa风矢量流线图
q1 = ax1.streamplot(lon, lat, u, v,density=[1, 5],transform=ccrs.PlateCarree())
plt.show()
