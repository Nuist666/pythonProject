import matplotlib.pyplot as plt
import numpy as np

rng = np.random.RandomState(0).rand(5)
markers = ['o', '+', '*', 's', '<']
labels = ['CNRM-CM3', 'GFDL-CM2.0', 'GISS-AOM', 'MIROC3.2', 'CCSM3', ]
#绘制散点图
fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
#通过循环，每次绘制一种标记的散点，循环5次
for i in range(5):
    ax1.scatter(rng, rng, marker=markers[i], label=labels[i])
ax1.legend()
plt.show()
