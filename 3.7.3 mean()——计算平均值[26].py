# 计算数组均值
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a.mean())
print(a.mean(axis=(0, 1)))
print('由于数组a只有两个维度，所以axis=(0, 1)等价于对所有维度取平均值')
print(a.mean(axis=0))
print(a.mean(axis=1))
