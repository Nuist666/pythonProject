import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import cartopy.mpl.ticker as cticker
import pandas as pd
import numpy as np

#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
z = f['hgt'].loc['2005-01-01':'2005-12-01', 500, :, 120]
time = z.time
lat = z.lat
#创建Figure
fig = plt.figure(figsize=(16, 13))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(1, 1, 1)
#绘制等值线
q1 = ax1.contour(range(time.shape[0]), lat, z.T)
#设置y轴为对数坐标轴，并设置相关标签
ax1.set_xticks(np.arange(0, 12, 1))
ax1.set_yticks(np.arange(-90, 120, 30))
ax1.yaxis.set_major_formatter(cticker.LatitudeFormatter())
#设置x轴标签
ax1.set_xlim(0, 11)
ax1.set_xticks(np.arange(0, 12, 1))
ax1.set_xticklabels(pd.date_range(start='2005-01', periods=12, freq='M').date)
#添加图题
ax1.set_title('2005 500hPa Z', loc='center', fontsize=18)
plt.show()
