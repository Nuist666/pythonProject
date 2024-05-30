import pandas as pd
import xarray as xr
import numpy as np
#构造数组
da = xr.DataArray(np.abs(np.random.randn(3, 3, 3)*5+15),coords=[pd.to_datetime(['2020-02-19', '2020-02-20', '2020-02-22']),[20, 25, 30], [120, 125, 130]],dims=['time', 'lat', 'lon'])
print(da)
da_interp = da.interp(time=['2020-02-21'], method='linear')
print(da_interp)
