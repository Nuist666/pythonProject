# 二进制文件的写入
import numpy as np

a = np.array([[10.5, 13, 16.3],
              [12, 12.5, 15.5],
              [11.3, 12.2, 15.4]])
print(a.dtype)  # 输出结果为float64
a.tofile('binary_raw.bin')
