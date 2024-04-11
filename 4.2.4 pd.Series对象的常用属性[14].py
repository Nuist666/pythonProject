# 通过布尔序列列访问多个元素
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2], index=['a', 'b', 'c', 'd'], name='t')
print(a.loc[[True, False, True, False]])
