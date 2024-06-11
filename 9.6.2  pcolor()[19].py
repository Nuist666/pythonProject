import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import numpy as np
import cartopy.mpl.ticker as cticker

#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
z = f['hgt'].loc['2005-07-01', 500, :, :]
t = f['air'].loc['2005-07-01', 700, :, :]
lat = f['lat']
lon = f['lon']
#创建Figure
fig = plt.figure(figsize=(15, 12))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(2, 2, 1, projection=ccrs.PlateCarree())
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
c1 = ax1.pcolor(lon, lat, t, vmin=-20, vmax=20, cmap='bwr', zorder=1, transform=ccrs.PlateCarree())
#添加图题
ax1.set_title('(a) July 2005 500hPa T', loc='center', fontsize=18)
#添加色标
fig.colorbar(c1, ax=ax1, fraction=0.032)
#ax2
ax2 = fig.add_subplot(2, 2, 2, projection=ccrs.PlateCarree())
#设置ax2的范围
ax2.set_extent([60, 180, 0, 90])
#为ax2添加海岸线
#ax2.coastlines()
#为ax2添加地理经纬度标签及刻度
ax2.set_xticks(np.arange(60, 210, 30), crs=ccrs.PlateCarree())
ax2.set_yticks(np.arange(0, 90, 30), crs=ccrs.PlateCarree())
ax2.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax2.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#将700hPa温度场绘制为填色等值线图
c2 = ax2.pcolor(lon, lat, t, vmin=-20, vmax=20, cmap='bwr', zorder=1, edgecolors='k', transform=ccrs.PlateCarree())
#添加图题
ax2.set_title('(b) July 2005 500hPa T', loc='center', fontsize=18)
#添加色标
fig.colorbar(c2, ax=ax2, fraction=0.032)
#创建一个t_copy数组并将大于15的数据设置为缺测
t_copy = t.values.copy()
t_copy[t_copy > 15] = np.nan
#ax3
ax3 = fig.add_subplot(2, 2, 3, projection=ccrs.PlateCarree())
#设置ax3的范围
ax3.set_extent([60, 180, 0, 90])
#为ax3添加海岸线
#ax3.coastlines()
#为ax3添加地理经纬度标签及刻度
ax3.set_xticks(np.arange(60, 210, 30), crs=ccrs.PlateCarree())
ax3.set_yticks(np.arange(0, 90, 30), crs=ccrs.PlateCarree())
ax3.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax3.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#将700hPa温度场绘制为填色等值线图
c3 = ax3.contourf(lon, lat, t_copy, levels=np.arange(-21, 22, 1), extend='both', cmap='bwr', zorder=1,
                  transform=ccrs.PlateCarree())
#添加图题
ax3.set_title('(c) July 2005 500hPa T', loc='center', fontsize=18)
#添加色标
fig.colorbar(c3, ax=ax3, fraction=0.032)
#ax4
ax4 = fig.add_subplot(2, 2, 4, projection=ccrs.PlateCarree())
#设置ax4的范围
ax4.set_extent([60, 180, 0, 90])
#为ax4添加海岸线
#ax4.coastlines()
#为ax4添加地理经纬度标签及刻度
ax4.set_xticks(np.arange(60, 210, 30), crs=ccrs.PlateCarree())
ax4.set_yticks(np.arange(0, 90, 30), crs=ccrs.PlateCarree())
ax4.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax4.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#将700hPa温度场绘制为填色等值线图
c4 = ax4.pcolor(lon, lat, t_copy, vmin=-20, vmax=20, cmap='bwr', zorder=1, edgecolors='k', transform=ccrs.PlateCarree())
#添加图题
ax4.set_title('(d) July 2005 500hPa T', loc='center', fontsize=18)
#添加色标
fig.colorbar(c4, ax=ax4, fraction=0.032)
plt.show()
