import pandas as pd
#构造数组
df = pd.DataFrame([[21.7, 983, 0.64],
                  [19.2, 991, 0.75],
                  [13.4, 973, 0.83]],
                 columns=['t', 'p', 'rh']
                )
df['time'] = pd.to_datetime(['2020-02-19', '2020-02-20', '2020-02-22'])
print(df)
df = df.set_index('time')
print(df)
df_interp = df.resample('1D').interpolate(method='linear')
print(df_interp)
