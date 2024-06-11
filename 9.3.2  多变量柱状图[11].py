import numpy as np
import matplotlib.pyplot as plt

#生成数据
labels = ['A', 'B', 'C', 'D']
v1 = np.array([20, 35, 30, 35])
v2 = np.array([25, 32, 34, 20])
v3 = np.array([11, 14, 20, 18])
v1_std = np.array([2, 3, 4, 1])
v2_std = np.array([3, 5, 2, 3])
v3_std = np.array([2, 3, 4, 1])
width = 0.35
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1, 1, 1)
#绘制垂直堆叠的多变量柱状图
ax1.bar(labels, v1, width, yerr=v1_std, label='v1')
ax1.bar(labels, v2, width, yerr=v2_std, bottom=v1, label='v2')
ax1.bar(labels, v3, width, yerr=v3_std, bottom=v2 + v1, label='v3')
ax1.legend()
plt.show()
