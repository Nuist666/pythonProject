import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#读取数据
ao = pd.read_csv("AO.txt", sep='\s+', header=None, names=['year', 'month', 'AO'])
ao_jan = ao[ao.month == 1]
#创建Figure及Axes
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(1, 1, 1)
ax1.set_title('1950-2019 January AO Index')
#绘制单变量柱状图
ax1.bar(np.arange(1950, 2020, 1), ao_jan.AO)
#添加0值参考线
ax1.axhline(0, c='k')
plt.show()
