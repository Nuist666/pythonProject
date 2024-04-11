# 计算数组元素标准差
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a.std())
print(a.std(axis=(0, 1)))
print(a.std(axis=0))
