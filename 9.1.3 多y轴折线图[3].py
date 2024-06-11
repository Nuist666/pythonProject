import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#读取数据
ao = pd.read_csv("AO.txt", sep='\s+', header=None, names=['year', 'month', 'AO'])
ao_jan = ao[ao.month == 1]
ao_feb = ao[ao.month == 2]
#创建Figure
fig = plt.figure()
#绘制单y轴折线图
ax1 = fig.add_subplot(1, 1, 1)
ax1.plot(np.arange(1950, 2020, 1), ao_jan.AO, 'ko-', label='Jan')
ax1.set_ylabel('January', c='r')
ax1.set_title('1950-2019 AO Index')
#创建第二个y轴
ax2 = ax1.twinx()
ax2.plot(np.arange(1950, 2020, 1), ao_feb.AO, 'rs-', label='Feb')
ax2.set_ylim(-4, 4)
ax2.set_ylabel('February', c='k')
#添加图例
plt.show()
