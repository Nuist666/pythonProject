# 按照索引的运算
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2], index=['a', 'b', 'c', 'd'], name='t1')
b = pd.Series([9.1, 9.5, 10.0, 11.2], index=['b', 'a', 'c', 'd'], name='t2')
print(b - a)
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2], index=['a', 'b', 'c', 'd'], name='t1')
b = pd.Series([9.1, 9.5, 10.0, 11.2], index=['b', 'c', 'd', 'e'], name='t2')
print(b - a)
import pandas as pd

a = pd.Series([9.1, 9.5, 10.0, 11.2], index=['a', 'b', 'c', 'd'], name='t1')
b = pd.Series([9.1, 9.5, 10.0, 11.2], index=['e', 'f', 'g', 'h'], name='t2')
print(b - a)
