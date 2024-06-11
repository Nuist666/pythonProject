import pandas as pd
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import cartopy.io.shapereader as shpreader
import numpy as np

data = pd.read_csv("825station.txt", sep='\s+', header=None, names=['stat', 'lat', 'lon', 'high'])
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree(central_longitude=105))
#设置图形范围及刻度
ax1.set_extent([70, 110, 30, 60], crs=ccrs.PlateCarree())
ax1.set_xticks(np.arange(70, 120, 10), crs=ccrs.PlateCarree())
ax1.set_yticks(np.arange(30, 70, 10), crs=ccrs.PlateCarree())
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#绘制站点的三维分布图
s = ax1.scatter(data.lon, data.lat, s=5, c=data.high, cmap='jet', transform=ccrs.PlateCarree())
#添加色标，fraction参数用于设置色标缩放比例
fig.colorbar(s, ax=ax1, fraction=0.034)
#添加海岸线等特征
ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))
china = shpreader.Reader('bou2_4l.dbf').geometries()
ax1.add_geometries(china, ccrs.PlateCarree(),facecolor='none', edgecolor='black',zorder = 1)
plt.show()
