# 利用逻辑索引取出符合条件的元素
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
print(a[a > 4])
print(a[(a > 4) & (a < 8)])
