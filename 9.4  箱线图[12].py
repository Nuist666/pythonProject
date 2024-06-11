import matplotlib.pyplot as plt
import numpy as np

#生成数据
data = [np.random.normal(0, std, 100) for std in range(1, 4)]
#绘制箱线图
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1, 1, 1)
ax1.boxplot(data, vert=True, whis=1.2, patch_artist=True, boxprops={'color': 'black', 'facecolor': 'red'})
plt.show()
