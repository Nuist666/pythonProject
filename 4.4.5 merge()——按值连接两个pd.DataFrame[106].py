# 按值连接两个pd.DataFrame
import pandas as pd

a = pd.DataFrame([['sunny', 983, 0.64],
                  ['rain', 991, 0.75],
                  ['fog', 973, 0.83],
                  ['haze', 1001, 0.93]],
                 index=['d1', 'd2', 'd3', 'd4'],
                 columns=['weather', 'p', 'rh']
                 )
b = pd.DataFrame([['rain', '0121'],
                  ['windy', '1123'],
                  ['fog', '1234'],
                  ['sunny', '2234']],
                 columns=['weather', 'code']
                 )
print(a)
print('------')
print(b)
# 左连接
c = pd.merge(left=a, right=b, left_on='weather', right_on='weather', how='left')
print(c)
# 右连接
c = pd.merge(left=a, right=b, left_on='weather', right_on='weather', how='right')
print(c)
# 内连接
c = pd.merge(left=a, right=b, left_on='weather', right_on='weather', how='inner')
print(c)
# 外连接
c = pd.merge(left=a, right=b, left_on='weather', right_on='weather', how='outer')
print(c)
