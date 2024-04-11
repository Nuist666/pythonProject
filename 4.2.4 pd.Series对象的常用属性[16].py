# 获取数据的原始np.ndarray对象
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2], index=['a', 'b', 'c', 'd'], name='t')
b = a.values
print(b)
print(type(b))
