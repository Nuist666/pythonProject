import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import numpy as np

#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
u = f['uwnd'].loc['2005-01-01':'2005-12-01', :, 35, 120]
w = f['omega'].loc['2005-01-01':'2005-12-01', :, 35, 120]
time = u.time
lev = u.level
#创建Figure
fig = plt.figure(figsize=(16, 13))
#绘制500hPa位势高度场
ax1 = fig.add_subplot(1, 1, 1)
#绘制500hPa水平风场
q1 = ax1.quiver(range(time.shape[0]), lev, u, w * 200, pivot='mid')
#添加参考矢量
ax1.quiverkey(q1, 0.9, 1.01, U=30, label='30m/s')
#设置y轴为对数坐标轴，并设置相关标签
ax1.set_yscale('symlog')
ax1.set_xticks(np.arange(0, 12, 1))
ax1.set_yticks([1000, 850, 700, 500, 300, 200, 100])
ax1.set_yticklabels([1000, 850, 700, 500, 300, 200, 100])
ax1.set_ylim(1050, 90)
#设置x轴标签
ax1.set_xlim(-1, 12)
ax1.set_xticks(np.arange(0, 12, 1))
ax1.set_xticklabels(pd.date_range(start='2005-01', periods=12, freq='M').date)
#添加图题
ax1.set_title('2005 U&OMEGA', loc='center', fontsize=18)
plt.show()
