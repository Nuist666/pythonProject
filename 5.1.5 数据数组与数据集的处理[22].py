# 邻近模糊索引
import xarray as xr

da = xr.DataArray([1, 2, 3], [("x", [0, 1, 2])])
print(da)
print(da.sel(x=[1.1, 1.9], method="nearest"))
print(da.sel(x=0.1, method="backfill"))
print(da.sel(x=[0.5, 1, 1.5, 2, 2.5], method="pad"))
