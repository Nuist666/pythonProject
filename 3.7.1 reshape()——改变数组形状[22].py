# 利用特殊值-1自动计算长度
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
print(a.shape)
b = a.reshape(2, -1)
print(b)
print(b.shape)
