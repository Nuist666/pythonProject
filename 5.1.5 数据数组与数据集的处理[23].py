# 使用tolerance参数设置模糊索引允许的最大偏差范围
import xarray as xr

da = xr.DataArray([1, 2, 3], [("x", [0, 1, 2])])
print(da.reindex(x=[0.9, 1.1, 1.5], method="nearest", tolerance=0.2))
