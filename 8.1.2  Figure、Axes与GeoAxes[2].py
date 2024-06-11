import numpy as np
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(12,6))
for i in range(6):
    ax=fig.add_subplot(2,3,i+1)
    ax.text(0.5,0.5,f'{i+1}', fontsize=20,ha='center',va='center')
    ax.text(0.5,0.2,f'ax=fig.add_subplot(2,3,{i+1})', fontsize=10,ha='center',va='center')
ax = fig.add_axes([0.3, 0.35, 0.3, 0.2])
ax.text(0.5,0.5,'ax=fig.add_axes([0.3, 0.35, 0.2, 0.2])', fontsize=10, ha='center', va='center')
# 这里的[0.3, 0.35, 0.2, 0.2]指Axes的左轴距离左边界0.3个Figure的宽度，
# 下轴距离下边界0.35个Figure的高度，Axes宽度为0.2个Figure的宽度，
# Axes的高度为0.2个Figure的高度
fig.show()
