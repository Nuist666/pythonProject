import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import pandas as pd
import numpy as np
#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
t = f['air'].loc['2005-07-01',:,:,80:150].mean('lon')
lev = t.level
lat = t.lat
#创建Figure
fig = plt.figure(figsize=(10, 8))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(1,1,1)
#绘制温度场垂直剖面
c1 = ax1.contour(lat, lev, t,colors='k')
ax1.clabel(c1, fmt='%d', fontsize=14.5,inline=True)
#设置y轴为对数坐标轴，并设置相关标签
ax1.set_yscale('symlog')
ax1.set_xticks(np.arange(0,12,1))
ax1.set_yticks([1000,850,700,500,300,200,100])
ax1.set_yticklabels([1000,850,700,500,300,200,100])
ax1.set_ylim(1000,100)
#为ax1的x轴添加地理经纬度标签及刻度
ax1.set_xticks(np.arange(-90,120,30))
ax1.xaxis.set_major_formatter(cticker.LongitudeFormatter())
#添加图题
ax1.set_title('July 2005 T',loc='center',fontsize=18)
plt.show()
