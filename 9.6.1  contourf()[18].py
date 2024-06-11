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
ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
#设置ax1的范围
ax1.set_extent([60, 180, 0, 90])
#为ax1添加海岸线
#ax1.coastlines()
#为ax1添加地理经纬度标签及刻度
ax1.set_xticks(np.arange(60, 210, 30), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(0, 90, 30), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#将700hPa温度场绘制为填色等值线图
c1 = ax1.contourf(lon, lat, t, levels=np.arange(-21, 22, 1), extend='both', cmap='bwr', zorder=1,
                  transform=ccrs.PlateCarree())
#把温度大于(小于)10(-10)℃的区域覆盖上阴影，100(-100)可以换为更大或更小的数，只是用于表明区间
c2 = ax1.contourf(lon, lat, t, levels=[-100, -10, 10, 100], hatches=['//', None, '//'], zorder=2, colors='none',
                  transform=ccrs.PlateCarree())
#从5000到5880每间隔80绘制一条黑色的等值线
c3 = ax1.contour(lon, lat, z, levels=np.arange(5000, 5880, 80), colors='k', zorder=3, transform=ccrs.PlateCarree())
#为c1添加数值标签，标签格式为整型
ax1.clabel(c3, fmt='%d', fontsize=14.5, inline=True)
#单独绘制加粗并且用虚线表示的5880副高特征线
c4 = ax1.contour(lon, lat, z, levels=[5880], colors='k', zorder=4, transform=ccrs.PlateCarree(), linewidths=3,
                 linestyles='--')
#为c2添加数值标签，标签格式为浮点型（保留一位小数）
ax1.clabel(c4, fmt='%d', fontsize=14.5, inline=True)
#添加图题
ax1.set_title('July 2005 500hPa Z&T', loc='center', fontsize=18)
#添加色标
fig.colorbar(c1, ax=ax1, fraction=0.032)
plt.show()
