# 保存为CSV文件
import pandas as pd

a = pd.Series([-9.5, 10.1, -11.2, 10.0],
              index=['a', 'b', 'c', 'd'],
              name='t')
a.to_csv('series_with_index.csv')
