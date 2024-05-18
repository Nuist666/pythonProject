# 数据维度的堆栈与出栈
import xarray as xr
import numpy as np

array = xr.DataArray(np.random.randn(2, 3), coords=[("x", ["a", "b"]), ("y", [0, 1, 2])])
print(array)
# 对数据的x和y维度进行堆叠
stacked = array.stack(z=("x", "y"))
print(stacked)
# 使用unstack()方法将堆叠的数据拆分
print(stacked.unstack("z"))
