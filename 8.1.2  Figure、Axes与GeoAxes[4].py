import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import numpy as np

f = xr.open_dataset('/home/nuist666/下载/data/1980060106.nc')
z = f['z'].loc[:,500,:,:][0]
lat = f['latitude']
lon = f['longitude']
plt.figure(figsize=(8, 6))
ax1 = plt.subplot(1,1,1, projection=ccrs.PlateCarree())
ax1.set_extent([60,180,0,90]) #设置GeoAxes的范围，4个数字分别代表左、右、上、下边界的经纬度
ax1.gridlines() #添加栅格线
#ax1.coastlines() #添加海岸线
#ax1.add_feature(cfeature.LAND) #添加大陆特征
#添加刻度
ax1.set_xticks(np.arange(60,210,30), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(0,120,30), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#绘制等值线
c1 = ax1.contour(lon, lat, z,transform=ccrs.PlateCarree())
plt.show()
