from matplotlib.projections import PolarAxes
from mpl_toolkits.axisartist import floating_axes
from mpl_toolkits.axisartist import grid_finder
import numpy as np
import matplotlib.pyplot as plt
#绘制泰勒图坐标系
def set_tayloraxes(fig, location):
#新建极坐标系
    trans = PolarAxes.PolarTransform()
#相关系数轴
    r1_locs = np.hstack((np.arange(1,10)/10.0,[0.95,0.99]))
    t1_locs = np.arccos(r1_locs)
    gl1 = grid_finder.FixedLocator(t1_locs)
    tf1 = grid_finder.DictFormatter(dict(zip(t1_locs, map(str,r1_locs))))
#标准差轴
    r2_locs = np.arange(0,2,0.25)
    r2_labels = ['0 ', '0.25 ', '0.50 ', '0.75 ', 'REF ', '1.25 ', '1.50 ', '1.75 ']
    gl2 = grid_finder.FixedLocator(r2_locs)
    tf2 = grid_finder.DictFormatter(dict(zip(r2_locs, map(str,r2_labels))))
    ghelper = floating_axes.GridHelperCurveLinear(trans,extremes=(0,np.pi/2,0,1.75),
                                                  grid_locator1=gl1,tick_formatter1=tf1,
                                                  grid_locator2=gl2,tick_formatter2=tf2)
    ax = floating_axes.FloatingSubplot(fig, location, grid_helper=ghelper)
    fig.add_subplot(ax)
#设置各个轴的格式
    ax.axis["top"].set_axis_direction("bottom")
    ax.axis["top"].toggle(ticklabels=True, label=True)
    ax.axis["top"].major_ticklabels.set_axis_direction("top")
    ax.axis["top"].label.set_axis_direction("top")
    ax.axis["top"].label.set_text("Correlation")
    ax.axis["top"].label.set_fontsize(14)
    ax.axis["left"].set_axis_direction("bottom")
    ax.axis["left"].label.set_text("Standard deviation")
    ax.axis["left"].label.set_fontsize(14)
    ax.axis["right"].set_axis_direction("top")
    ax.axis["right"].toggle(ticklabels=True)
    ax.axis["right"].major_ticklabels.set_axis_direction("left")
    ax.axis["bottom"].set_visible(False)
    ax.grid(True)
    polar_ax = ax.get_aux_axes(trans)

    rs,ts = np.meshgrid(np.linspace(0,1.75,100),
                            np.linspace(0,np.pi/2,100))
    rms = np.sqrt(1 + rs**2 - 2*rs*np.cos(ts))
    CS = polar_ax.contour(ts, rs,rms,colors='gray',linestyles='--')
    plt.clabel(CS, inline=1, fontsize=10)
    t = np.linspace(0,np.pi/2)
    r = np.zeros_like(t) + 1
    polar_ax.plot(t,r,'k--')
#将垂直轴的REF改为1.00
    polar_ax.text(np.pi/2+0.032,1.02, " 1.00", size=10.3,ha="right", va="top",
                  bbox=dict(boxstyle="square",ec='w',fc='w'))
    return polar_ax
#在泰勒图上绘制数据点
def plot_taylor(axes, refsample, sample, *args, **kwargs):
    std = np.std(refsample)/np.std(sample)
    corr = np.corrcoef(refsample, sample)
    theta = np.arccos(corr[0,1])
    t,r = theta,std
    d = axes.plot(t,r, *args, **kwargs)
    return d
x = np.linspace(0,100*np.pi,100)
#生成观测数据
data = np.sin(x)
#生成3组与原始数据形状相同的对比数据
m1 = data + 0.4*np.random.randn(len(x))
m2 = 0.3*data + 0.6*np.random.randn(len(x))
m3 = np.sin(x-np.pi/10)
#绘图
fig = plt.figure(figsize=(10,4))
ax1 = set_tayloraxes(fig, 121)
d1 = plot_taylor(ax1,data,m1, 'bo')
d2 = plot_taylor(ax1,data,m2, 'ro')
d3 = plot_taylor(ax1,data,m3, 'go')
plt.show()