import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
ao = pd.read_csv("AO.txt",sep='\s+',header=None, names=['year','month','AO'])
ao_jan = ao[ao.month==1]
ao_feb = ao[ao.month==2]
fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(2,1,1)
#绘制第一个序列
ax1.plot(np.arange(1950,2020,1),ao_jan.AO,'ko-',label='Jan')
#绘制第二个序列
ax1.plot(np.arange(1950,2020,1),ao_feb.AO,'rs-',label='Feb')
ax1.set_title('1950-2019 AO Index')
#添加图例
ax1.legend()
plt.show()
