# 计算数组元素之和
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a.sum())
print(a.sum(axis=(0, 1)))
print(a.sum(axis=0))
