import numpy as np
import matplotlib.pyplot as plt
#生成数据
x = np.arange(-10,10,0.01)
y = np.arange(-10,10,0.01)
x_grid,y_grid = np.meshgrid(x,y)
z = x_grid**2+y_grid**2
#创建Figure及Axes
fig1 = plt.figure(figsize=(10, 8))
#基础填色图
ax1 = fig1.add_subplot(2,2,1)
ca = ax1.contourf(x,y,z)
ax1.set_title('a')
fig1.colorbar(ca,ax=ax1)
#填充等值线图
ax2 = fig1.add_subplot(2,2,2)
cb1 = ax2.contour(x,y,z,colors="k")
cb2 = ax2.contourf(x,y,z,hatches=['.',',,','-', '/', '\\', '//'],colors="none")
ax2.set_title('b')
fig1.colorbar(ca,ax=ax2)
#特定level值的填色图1
ax3 = fig1.add_subplot(2,2,3)
cc = ax3.contourf(x,y,z,levels=np.arange(60,150,30))
ax3.set_title('c')
fig1.colorbar(cc,ax=ax3)
#特定level值的填色图2
ax4 = fig1.add_subplot(2,2,4)
cd = contour = ax4.contourf(x,y,z,levels=np.arange(60,150,30),extend='both')
ax4.set_title('d')
fig1.colorbar(cd,ax=ax4)
plt.show()
