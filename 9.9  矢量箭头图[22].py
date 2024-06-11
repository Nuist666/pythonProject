import matplotlib.pyplot as plt
fig = plt.figure(figsize=(15, 3))
ax1 = fig.add_subplot(1,2,1)
# 默认
q1 = ax1.quiver(0, 0, 1, 1)
# scale：缩放比例，值越大，箭头越短
q2 = ax1.quiver(0.1, 0, 1, 1, scale=15)
# width：主轴宽度
q3 = ax1.quiver(0.2, 0, 1, 1, width=0.05)
# headwidth：矢量符号箭头头部的宽度
q4 = ax1.quiver(0.3, 0, 1, 1, headwidth=8)
# headlength：矢量符号箭头头部的长度，从头部到尾部
q5 = ax1.quiver(0.4, 0, 1, 1, headlength=8)
# headaxislength 矢量符号箭头的头部到矢量符号轴和箭头的交接处的长度
q6 = ax1.quiver(0.5, 0, 1, 1, headwidth=8, headlength=8, headaxislength=2)
# minlength 最小箭头长度，当矢量长度小于此值时，矢量将被替换为正六边形
q7 = ax1.quiver(0.65, 0, 1, 1, headwidth=4, headlength=4, minlength=10)
ax1.set_axis_off()
plt.show()