# 保存为CSV文件
import pandas as pd

a = pd.DataFrame([[-21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, -973, -0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
a.to_csv('dataframe_to.csv')
