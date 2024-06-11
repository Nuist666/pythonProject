import numpy as np
# MetPy中用于绘制探空图的类
from metpy.plots import SkewT
from metpy.units import units
from metpy.calc import lcl
from metpy.calc import parcel_profile
import matplotlib.pyplot as plt

# 探空数据，原始的np.ndarray数组需要带上单位，转换为带单位的数据
# 气压层
p = np.array([1000, 925, 850, 700, 600, 500, 450, 400, 300, 250]) * units.hPa
# 气压层对应温度
t = np.array([4, 8, 3, -11, -21, -26, -33, -38, -55, -60]) * units.degC
# 气压层对应露点
td = np.array([-8, -9, -14, -18, -25, -34, -38, -43, -61, -67]) * units.degC
# 气压层对应风的U分量
u = np.array([-0.39, 0.11, 3.1, 10.7, 16.61, 24.0, 20.31, 33.43, 49.32, 59.21]) * units('m/s')
# 气压层对应风的V分量
v = np.array([-0.57, -0.75, -1.09, -0.79, -0.48, -0.04, -0.26, 0.96, 2.87, 4.14]) * units('m/s')
# 计算气块绝热抬升参数
prof = parcel_profile(p, t[0], td[0]).to('degC')
# 用最底层气压(这里是1000hPa)、温度和露点，计算抬升凝结高度对应的气压和温度
lcl_pressure, lcl_temperature = lcl(p[0], t[0], td[0])
fig = plt.figure(figsize=(8, 7))
# 用于绘制探空图的绘图实例
skew = SkewT(fig)
# 绘制气块绝热抬升路径
skew.plot(p, prof, 'k')
# 在图上标出抬升凝结高度和对应温度所在的点
skew.plot(lcl_pressure, lcl_temperature, 'ko', markerfacecolor='black')
# 绘制CIN阴影部分
skew.shade_cin(p, t, prof)
# 绘制CAPE阴影部分
skew.shade_cape(p, t, prof)
# 绘制0℃等温线
skew.ax.axvline(0, color='c', linestyle='--', linewidth=1)
# 环境温度垂直廓线
skew.plot(p, t, 'r')
# 环境露点垂直廓线
skew.plot(p, td, 'g')
# 高度层对应水平风场(原始风向杆等级划分不适用于国内标准)
barb_increments = {'half': 2, 'full': 4, 'flag': 20}
skew.plot_barbs(p, u, v, barb_increments=barb_increments)
# 绘制干绝热线
skew.plot_dry_adiabats(t0=np.arange(233, 533, 10) * units.K, alpha=0.5, color='orangered', linewidth=0.7)
# 绘制湿绝热线
skew.plot_moist_adiabats(t0=np.arange(233, 400, 5) * units.K, alpha=0.5, color='tab:green', linewidth=0.7)
# 绘制混合比线
skew.plot_mixing_lines(pressure=np.arange(1000, 99, -20) * units.hPa, linestyle='dotted', color='tab:blue',
                       linewidth=0.7)
#设置Y轴(高度层)范围
skew.ax.set_ylim(1000, 250)
#设置X轴(温度)范围
skew.ax.set_xlim(-40, 50)
plt.show()
