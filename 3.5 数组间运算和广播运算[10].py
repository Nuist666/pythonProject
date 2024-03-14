# 对于一维数组和二维数组之间的运算
import numpy as np

a = np.array([1, 2, 3])
b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [0, 1, 2],
              [3, 4, 5]])
print(a.shape)
print(b.shape)
c = a + b
print(c)
print(c.shape)
