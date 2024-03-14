# 多维数组的逻辑运算
import numpy as np

t1 = np.array([[10.5, 13, 16.3],
               [12, 12.5, 15.5]])
print((t1 > 12) | (t1 < 11))
print((t1 > 12) & (t1 < 13))
