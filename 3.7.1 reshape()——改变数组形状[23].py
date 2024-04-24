# 利用特殊值-1展开数组
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a)
print(a.shape)
b = a.reshape(-1)
print(b)
print(b.shape)
