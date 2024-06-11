import numpy as np
import matplotlib.pyplot as plt
#生成正弦函数
x = np.linspace(0, 10, 500)
y = np.sin(x)
#绘制图像
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1,1,1)
ax1.plot(x, y)
plt.savefig('./sinx.png', dpi=400, bbox_inches='tight')