# 二进制文件的读入
import numpy as np

a = np.fromfile('binary_raw.bin', dtype=np.float64)
print(a)
a = a.reshape((3, 3))
print(a)
