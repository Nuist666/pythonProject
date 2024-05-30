import xarray as xr
from pykrige.ok import OrdinaryKriging
import pandas as pd
import numpy as np

df = pd.read_csv('r160.txt', sep='\s+', names=['lat', 'lon', 'pre_ano'])
krige = OrdinaryKriging(
    df['lon'],
    df['lat'],
    df['pre_ano'],
    variogram_model="linear",
    verbose=False,
    enable_plotting=False,
)
lon = np.arange(76.0, 131.5+0.5, 0.5) # np.arange()函数创建的数组不包含参数传入的终点值
lat = np.arange(20.5, 51.5+0.5, 0.5) # 所以在终点值后再加入一个步长以确保最后一个值被包含在结果中
pre_grid, ss = krige.execute("grid", lon, lat)
pre_da = xr.DataArray(pre_grid, coords=[lat, lon], dims=['lat', 'lon'])
print(pre_da)
