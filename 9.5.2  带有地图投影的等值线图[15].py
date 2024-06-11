import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import numpy as np

#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
z = f['hgt'].loc['2005-07-01', 500, :, :]
t = f['air'].loc['2005-07-01', 700, :, :]
lat = f['lat']
lon = f['lon']
#创建Figure
fig = plt.figure(figsize=(15, 12))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())
#设置ax1的范围
ax1.set_extent([60, 180, 0, 90])
#为ax1添加海岸线
#ax1.coastlines()
#为ax1添加地理经纬度标签及刻度
ax1.set_xticks(np.arange(60, 210, 30), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(0, 90, 30), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#从5000到5800每间隔80绘制一条黑色的等值线
c1 = ax1.contour(lon, lat, z, levels=np.arange(5000, 5880, 80), colors='k', transform=ccrs.PlateCarree())
#为c1添加数值标签，标签格式为整型
ax1.clabel(c1, fmt='%d', fontsize=14.5, inline=True)
#单独绘制加粗并且用虚线表示的5880副高特征线
c2 = ax1.contour(lon, lat, z, levels=[5880], colors='k', transform=ccrs.PlateCarree(), linewidths=3, linestyles='--')
#为c2添加数值标签，标签格式为浮点型（保留一位小数）
ax1.clabel(c2, fmt='%d', fontsize=14.5, inline=True)
#添加图题
ax1.set_title('July 2005 500hPa Z', loc='center', fontsize=18)
ax1.set_title('unit: gpm', loc='right', fontsize=18)
#绘制700hPa温度场
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree())
ax2.set_extent([60, 180, 0, 90])
#ax2.coastlines()
ax2.set_xticks(np.arange(60, 210, 30), crs=ccrs.PlateCarree())
ax2.set_yticks(np.arange(0, 90, 30), crs=ccrs.PlateCarree())
ax2.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax2.yaxis.set_major_formatter(cticker.LatitudeFormatter())
c3 = ax2.contour(lon, lat, t, levels=np.arange(-30, 33, 3), colors='k', transform=ccrs.PlateCarree())
ax2.clabel(c3, fmt='%.1f', fontsize=14.5, inline=True)
ax2.set_title('July 2005 700hPa T', loc='center', fontsize=18)
ax2.set_title('unit: $^\circ$C', loc='right', fontsize=18)
plt.show()
