import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

fig = plt.figure(figsize=[10, 5])
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.Mercator())
ax1.add_feature(cfeature.COASTLINE.with_scale('110m'))
gl1 = ax1.gridlines(draw_labels=True, x_inline=False, y_inline=False)  #添加栅格线
# 隐藏上、右坐标轴刻度
gl1.xlabels_top = False
gl1.ylabels_right = False
plt.show()
