# 指定顺序的交换
import numpy as np
a = np.zeros((10, 15, 25))
print(a.shape)
b = a.transpose(1, 0, 2)
print(b.shape)
