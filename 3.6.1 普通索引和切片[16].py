# 用于对索引位置赋值
import numpy as np
a = np.array([[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]])
a[1, 1] = 0
print(a)
