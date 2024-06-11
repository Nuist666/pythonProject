import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
fig = plt.figure(figsize=[10, 5])
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.NorthPolarStereo())
ax1.add_feature(cfeature.COASTLINE.with_scale('110m'))
gl1 = ax1.gridlines(draw_labels=True,x_inline=False, y_inline=True) #添加栅格线
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.SouthPolarStereo())
ax2.add_feature(cfeature.COASTLINE.with_scale('110m'))
gl2 = ax2.gridlines(draw_labels=True,x_inline=False, y_inline=True) #添加栅格线
plt.show()
