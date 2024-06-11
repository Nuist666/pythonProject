from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
#读取数据
ao = pd.read_csv("AO.txt",sep='\s+',header=None, names=['year','month','AO'])
ao_dec = ao[ao.month==12]
ao_jan = ao[ao.month==1]
ao_feb = ao[ao.month==2]
ao_djf = (ao_jan.AO.values+ao_feb.AO.values+ao_dec.AO.values)/3
#创建Figure
fig = plt.figure()
#创建主轴
ax = HostAxes(fig, [0, 0, 0.9, 0.9])  #[left, bottom, weight, height]
#创建共享x轴的其他y轴
ax1 = ParasiteAxes(ax, sharex=ax)
ax2 = ParasiteAxes(ax, sharex=ax)
ax3 = ParasiteAxes(ax, sharex=ax)
ax.parasites.append(ax1)
ax.parasites.append(ax2)
ax.parasites.append(ax3)
#将主轴的右轴隐藏，同时开始设置第二个轴的可见性
ax.axis['right'].set_visible(False)
ax1.axis['right'].set_visible(True)
ax1.axis['right'].major_ticklabels.set_visible(True)
ax1.axis['right'].label.set_visible(True)
#设置各轴的标签
ax.set_ylabel('DJF')
ax.set_xlabel('year')
ax1.set_ylabel('Dec')
ax2.set_ylabel('Jan')
ax3.set_ylabel('Feb')
#设置第三个和第四个y轴的位置
axisline2 = ax2.get_grid_helper().new_fixed_axis
axisline3 = ax3.get_grid_helper().new_fixed_axis
ax2.axis['right2'] = axisline2(loc='right', axes=ax2, offset=(40,0))
ax3.axis['right3'] = axisline3(loc='right', axes=ax3, offset=(80,0))
#将设置好的主轴的Axes放在Figure上
fig.add_axes(ax)
#绘制折线
ax.plot(np.arange(1950,2020,1), ao_djf, label="DJF", color='black')
ax1.plot(np.arange(1950,2020,1), ao_dec.AO, label="Dec", color='red')
ax2.plot(np.arange(1950,2020,1), ao_jan.AO, label="Jan", color='green')
ax3.plot(np.arange(1950,2020,1), ao_feb.AO, label="Feb", color='orange')
ax1.set_ylim(-4,4)
ax2.set_ylim(-5,5)
ax3.set_ylim(-6,6)
ax.legend()
#设置各个轴及其刻度的颜色
ax1.axis['right'].major_ticks.set_color('red')
ax2.axis['right2'].major_ticks.set_color('green')
ax3.axis['right3'].major_ticks.set_color('blue')
ax1.axis['right'].major_ticklabels.set_color('red')
ax2.axis['right2'].major_ticklabels.set_color('green')
ax3.axis['right3'].major_ticklabels.set_color('blue')
ax1.axis['right'].line.set_color('red')
ax2.axis['right2'].line.set_color('green')
ax3.axis['right3'].line.set_color('blue')
plt.show()