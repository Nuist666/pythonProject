# 引入绘图库
import numpy as np
import matplotlib.pyplot as plt
# 绘图数据计算函数
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)
# 生成两个子图对应的横轴数据
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
# 生成figure
plt.figure(1)
# 生成子图1(位置为两行一列排布的从上往下数第一个)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
# 生成子图2(位置为两行一列排布的从上往下数第二个)
plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
# 进行绘图
plt.show()
