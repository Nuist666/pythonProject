# pd.Series、pd.DataFrame以及pd.Panel来创建DataArray
import xarray as xr
import pandas as pd
df = pd.DataFrame({"lat": [0, 1], "lon": [2, 3]}, index=["2000-01-01", "2000-01-02"])
df.index.name = "time"
df.columns.name = "space"
print(df)
foo = xr.DataArray(df)
print(foo)
