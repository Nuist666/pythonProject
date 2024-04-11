# 尝试修改一个一维向量的形状
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a.shape)
b = a.reshape(2, 3)
print(b)
print(b.shape)
c = a.reshape(6, 1)
print(c)
print(c.shape)
