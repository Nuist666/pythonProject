# 使用np.arange()创建数组
import numpy as np

a = np.arange(5)
b = np.arange(3, 5)
c = np.arange(3, 5, 0.5)
d = np.arange(3, 5, 0.5, dtype=np.float32)
print(a)
print(a.dtype)
print(b)
print(b.dtype)
print(c)
print(c.dtype)
print(d)
print(d.dtype)
