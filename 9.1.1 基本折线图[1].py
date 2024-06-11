import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
#读取数据
ao = pd.read_csv("AO.txt",sep='\s+',header=None, names=['year','month','AO'])
ao_jan = ao[ao.month==1]
#创建Figure
fig = plt.figure(figsize=(10, 8))
#创建Axes
ax1 = fig.add_subplot(1,1,1)
#绘制折线图
ax1.plot(np.arange(1950,2020,1),ao_jan.AO, 'ko-')
#添加图题
ax1.set_title('1950-2019 January AO Index')
#添加y=0水平参考线
ax1.axhline(0,ls=':',c='r')
#添加x=1990垂直参考线
ax1.axvline(1990,ls='--',c='g')
plt.show()