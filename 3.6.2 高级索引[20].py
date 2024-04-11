# 花式索引
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a[[0, 2]])
print(a[[0, 2], [1, 2]])
