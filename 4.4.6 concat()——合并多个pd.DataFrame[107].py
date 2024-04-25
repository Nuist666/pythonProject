# 直接按照行或列合并多个pd.DataFrame
import pandas as pd

a = pd.DataFrame([['sunny', 983, 0.64],
                  ['rain', 991, 0.75],
                  ['fog', 973, 0.83],
                  ['haze', 1001, 0.93]],
                 index=['d1', 'd2', 'd3', 'd4'],
                 columns=['weather', 'p', 'rh']
                 )
print(pd.concat([a, a]))
print('-----')
print(pd.concat([a, a], axis=1))
