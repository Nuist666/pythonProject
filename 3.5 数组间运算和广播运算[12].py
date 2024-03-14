# 将向量化用于两个场之间的运算
import numpy as np

t1 = np.array([[10.5, 13, 16.3],
               [12, 12.5, 15.5]])
t2 = np.array([[8.4, 7.2, 5.5],
               [7.1, 7.0, 6.0]])
t_mean = (t1 + t2) / 2
print(t_mean)
