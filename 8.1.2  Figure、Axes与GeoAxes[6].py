import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
fig = plt.figure(figsize=[10, 5])
ax1 = fig.add_subplot(1, 2, 1, projection=ccrs.LambertConformal())
gl1 = ax1.gridlines(draw_labels=True,x_inline=False, y_inline=False) #添加栅格线，绘制刻度标签，但禁止在栅格线内绘制标签
gl1.rotate_labels = False #禁止刻度标签旋转
ax1.add_feature(cfeature.COASTLINE.with_scale('110m'))
ax2 = fig.add_subplot(1, 2, 2, projection=ccrs.LambertConformal(central_longitude=120,cutoff=0))
gl2 = ax2.gridlines(draw_labels=True,x_inline=False, y_inline=False) #添加栅格线
gl2.rotate_labels = False
ax2.add_feature(cfeature.COASTLINE.with_scale('110m'))
plt.show()
