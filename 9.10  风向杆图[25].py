import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import numpy as np

#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
u = f['uwnd'].loc['2005-07-01', 500, :, :].values
v = f['vwnd'].loc['2005-07-01', 500, :, :].values
lat = f['lat']
lon = f['lon']
#创建Figure
fig = plt.figure(figsize=(16, 13))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.Mercator())
#设置ax1的范围
ax1.set_extent([80, 140, 0, 40])
#为ax1添加海岸线
#ax1.coastlines()
#为ax1添加地理经纬度标签及刻度
ax1.set_xticks(np.arange(80, 160, 20), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(0, 60, 20), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#绘制500hPa水平风场
#Matplotlib原始的风向杆等级划分不适用于国内标准，所以需要额外指定符合标准的风向杆等级
barb_increments = {'half': 2, 'full': 4, 'flag': 20}
q1 = ax1.barbs(lon, lat, u, v, barb_increments=barb_increments, transform=ccrs.PlateCarree())
#添加图题
ax1.set_title('(a) July 2005 500hPa Wind', loc='center', fontsize=18)
plt.show()
