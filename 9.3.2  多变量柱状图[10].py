import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#数据读取
ao = pd.read_csv("AO.txt", sep='\s+', header=None, names=['year', 'month', 'AO'])
ao_dec = ao[ao.month == 12]
ao_jan = ao[ao.month == 1]
ao_feb = ao[ao.month == 2]
#创建Figure及Axes
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('2000—2019 DJF AO Index')
#绘制柱状图，ao_dec.AO[50:]表明从2000年开始绘制
ax1.bar(np.arange(2000, 2020, 1) - 0.25, ao_dec.AO[50:], width=0.25, color='r', label='Dec')
ax1.bar(np.arange(2000, 2020, 1), ao_jan.AO[50:], width=0.25, color='b', label='Jan')
ax1.bar(np.arange(2000, 2020, 1) + 0.25, ao_feb.AO[50:], width=0.25, color='g', label='Feb')
#添加0值参考线
ax1.axhline(0, c='k')
ax1.legend()
#由于多变量柱状图对应的x轴的刻度不一定为整数，因此我们指定x轴刻度以避免小数出现
ax1.set_xticks([2000, 2005, 2010, 2015, 2020])
plt.show()
