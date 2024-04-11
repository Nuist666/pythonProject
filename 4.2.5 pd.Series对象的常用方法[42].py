# 忽略元素名字和索引，只保存数据
import pandas as pd

a = pd.Series([-9.5, 10.1, -11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
a.to_csv('series_no_index.csv', index=False, header=False)
