import pandas as pd

df = pd.read_csv('r160.txt', sep='\s+', names=['lat', 'lon', 'pre_ano'])
print(df)
