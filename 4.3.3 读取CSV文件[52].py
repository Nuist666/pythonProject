# 读取只带有索引或列名的CSV文件
import pandas as pd

a = pd.read_csv('pandas_read_noheader.csv', header=None, index_col=0)
print(a)
import pandas as pd

a = pd.read_csv('pandas_read_noheader.csv',
                names=['sta', 't', 'p', 'rh'],
                index_col=0)
print(a)
