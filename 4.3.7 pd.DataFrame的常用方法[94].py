# 使用corrwith()计算pd.DataFram与另一个pd.Series或pd.DataFrame之间的相关系数
a = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
b = pd.DataFrame([[21.5, 988, 0.62],
                  [19.4, 996, 0.74],
                  [13.2, 973, 0.85]],
                 index=['s1', 's2', 's3'],
                 columns=['t', 'p', 'rh']
                 )
print(a)
print('--------')
print(a.corrwith(b))
