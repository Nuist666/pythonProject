# 对数组四舍五入
import numpy as np

a = np.array([[1.12, 2.25, 2.15],
              [4.03, 5.48, 6.75],
              [7.25, 7.35, 9.22]])
print(a.round())
print(a.round(1))
