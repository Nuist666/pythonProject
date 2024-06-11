import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import numpy as np

fig = plt.figure(figsize=[10, 5])
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.PlateCarree())
ax1.set_xticks(np.arange(-180, 240, 60), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(-90, 120, 30), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
ax1.gridlines()  #添加栅格线
ax1.add_feature(cfeature.COASTLINE.with_scale('110m'))
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.PlateCarree(central_longitude=120))
ax2.set_xticks(np.arange(-180, 240, 60), crs=ccrs.PlateCarree())
ax2.set_yticks(np.arange(-90, 120, 30), crs=ccrs.PlateCarree())
ax2.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax2.yaxis.set_major_formatter(cticker.LatitudeFormatter())
ax2.gridlines()  #添加栅格线
ax2.add_feature(cfeature.COASTLINE.with_scale('110m'))
plt.show()
