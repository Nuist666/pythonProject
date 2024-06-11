import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
# 样例数据生成，此段可以忽略
N = 100
X, Y = np.mgrid[-3:3:complex(0, N), -2:2:complex(0, N)]
Z1 = np.exp(-X**2 - Y**2)
Z2 = np.exp(-(X - 1)**2 - (Y - 1)**2)
Z = (Z1 - Z2) * 2
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
levels = [0.1, 0.3, 0.5, 0.9]
cmap = mcolors.ListedColormap(['r', 'g', 'b'])
cmap.set_under('c')
cmap.set_over('m')
norm = mcolors.BoundaryNorm(levels, cmap.N)
pcm = ax.contourf(Z, levels=levels, cmap=cmap, norm=norm, extend='both')
fig.colorbar(pcm, ax=ax, extend='both')
plt.show()
