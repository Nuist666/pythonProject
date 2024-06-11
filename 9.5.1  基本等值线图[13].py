import numpy as np
import matplotlib.pyplot as plt

#生成数据
x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)
x_grid, y_grid = np.meshgrid(x, y)
z = x_grid ** 2 + y_grid ** 2
#创建Figure及Axes
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(2, 2, 1)
ax1.contour(x, y, z)
ax1.set_title('a')
ax2 = fig.add_subplot(2, 2, 2)
ax2.contour(x, y, z, linestyles=':')
ax2.set_title('b')
ax3 = fig.add_subplot(2, 2, 3)
ax3.contour(x, y, z, levels=np.arange(60, 150, 30), linewidths=5)
ax3.set_title('c')
ax4 = fig.add_subplot(2, 2, 4)
contour = ax4.contour(x, y, z, levels=np.arange(60, 150, 30))
ax4.clabel(contour, fontsize=10, colors='k')
ax4.set_title('d')
plt.show()
