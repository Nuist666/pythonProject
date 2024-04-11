# 使用astype()方法根据需要生成新数据类型的多维数组
import numpy as np
a = np.array([1.2, 2.4, 3.5])
print(a.dtype)
b = a.astype(np.float32)
print(b.dtype)
c = a.astype(np.int_)
print(c.dtype)
print(c)
