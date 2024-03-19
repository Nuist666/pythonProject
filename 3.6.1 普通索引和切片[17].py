# 应用广播运算使用标量对切片赋值
import numpy as np
a = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
a[::2, :] = 0
print(a)
