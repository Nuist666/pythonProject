import pandas as pd
from pykrige.ok import OrdinaryKriging

df = pd.read_csv('r160.txt', sep='\s+', names=['lat', 'lon', 'pre_ano'])
krige = OrdinaryKriging(
    df['lon'],
    df['lat'],
    df['pre_ano'],
    variogram_model="linear",
    verbose=False,
    enable_plotting=False,
)
print(df)
