# 将数组所有元素修改为特定值
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
a[:] = 0
print(a)
