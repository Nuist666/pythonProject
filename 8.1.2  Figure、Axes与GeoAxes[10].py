import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np
import cartopy.crs as ccrs
import cartopy.feature as cfeature
fig = plt.figure(figsize=[5, 5])
ax1 = fig.add_subplot(1, 1, 1, projection=ccrs.NorthPolarStereo())
ax1.set_extent([-180, 180, 30, 90], ccrs.PlateCarree())
ax1.gridlines()
ax1.add_feature(cfeature.COASTLINE.with_scale('50m'))
# 生成一个圆形的Path
theta = np.linspace(0, 2*np.pi, 100)
center, radius = [0.5, 0.5], 0.5
verts = np.vstack([np.sin(theta), np.cos(theta)]).T
circle = mpath.Path(verts * radius + center)
# 将该Path设置为GeoAxes的边界
ax1.set_boundary(circle, transform=ax1.transAxes)
plt.show()
