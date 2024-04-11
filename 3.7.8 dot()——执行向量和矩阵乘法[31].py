# 矩阵乘法
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([[1, 2],
              [3, 4],
              [5, 6]])
print('shape_a=', a.shape)
print('shape_b=', b.shape)
c = a.dot(b)  # A×B
print(c)
