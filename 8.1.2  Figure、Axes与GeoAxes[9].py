import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
fig = plt.figure(figsize=[5, 5])
ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.NorthPolarStereo())
ax1.set_extent([-180, 180, 30, 90], ccrs.PlateCarree())
gl1 = ax1.gridlines(draw_labels=True,x_inline=False, y_inline=False) #添加栅格线
gl1.rotate_labels = False #禁止标签旋转，设置为True时标签与栅格线平行
ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))
plt.show()
