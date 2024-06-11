import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
f = xr.open_dataset('/home/nuist666/下载/data/1980060106.nc')
z = f['z'].loc[:,500,:,:][0] #取出第一个时刻的500hPa的位势场
lat = f['latitude']
lon = f['longitude']
plt.figure(figsize=(5, 5))
#ax1为Axes
ax1 = plt.subplot(1,2,1)
c1 = ax1.contour(lon, lat, z)
ax1.set_title('Axes')
#ax2为GeoAxes
ax2 = plt.subplot(1,2,2, projection=ccrs.PlateCarree())
c2 = ax2.contour(lon, lat, z,transform=ccrs.PlateCarree())
ax2.set_title('GeoAxes')
plt.show()