import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.mpl.ticker as cticker
import geopandas as gpd
import numpy as np

import geopandas as gpd
gdf = gpd.GeoDataFrame.from_file('circle.json', encoding='utf8')

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_extent([115.5, 123, 29.5, 36.5], ccrs.PlateCarree())
ax.add_geometries(gdf['geometry'], crs=ccrs.PlateCarree(), facecolor='none', edgecolor='black')
# 设置轴刻度
ax.set_xticks(np.arange(116, 123, 1), crs=ccrs.PlateCarree())
ax.set_yticks(np.arange(30, 36, 1), crs=ccrs.PlateCarree())
ax.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax.yaxis.set_major_formatter(cticker.LatitudeFormatter())
plt.show()
