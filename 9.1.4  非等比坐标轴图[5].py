import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import pandas as pd
import matplotlib.ticker as ticker
#读取数据
f = xr.open_dataset('/home/nuist666/下载/data/data.nc')
t = f['air'].loc['2005-07-01',:,45,120]
lev = t.level
#创建Figure
fig = plt.figure(figsize=(15,5))
#设置为log
ax1 = fig.add_subplot(1,3,1)
ax1.plot(t,lev)
ax1.set_ylim(1000,100)
ax1.set_yscale('log')
ax1.set_title('log')
ax1.set_yticks([1000,850,700,500,300,200,100])
ax1.set_yticklabels([1000,850,700,500,300,200,100])
#隐藏次坐标刻度
ax1.yaxis.set_minor_formatter(ticker.NullFormatter())
#设置为symlog
ax2 = fig.add_subplot(1,3,2)
ax2.plot(t,lev)
ax2.set_ylim(1000,100)
ax2.set_yscale('symlog')
ax2.set_title('symlog')
ax2.set_yticks([1000,850,700,500,300,200,100])
ax2.set_yticklabels([1000,850,700,500,300,200,100])
#设置为linear
ax3 = fig.add_subplot(1,3,3)
ax3.plot(t,lev)
ax3.invert_yaxis()
ax3.set_yscale('linear')
ax3.set_title('linear')
ax3.set_yticks([1000,850,700,500,300,200,100])
ax3.set_yticklabels([1000,850,700,500,300,200,100])
plt.show()
