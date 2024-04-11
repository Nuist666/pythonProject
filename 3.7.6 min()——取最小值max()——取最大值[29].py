# 获取元素最大和最小值
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a.max())
print(a.max(axis=(0, 1)))
print(a.max(axis=0))
print(a.min())
print(a.min(axis=(0, 1)))
print(a.min(axis=0))
