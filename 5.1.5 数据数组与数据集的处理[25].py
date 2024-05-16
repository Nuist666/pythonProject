# 缺测值处理
import xarray as xr
import numpy as np

x = xr.DataArray([0, 1, np.nan, np.nan, 2], dims=["x"])
print(x)
# 根据x中缺测值的位置返回布尔值
print(x.isnull())
# 根据x中非缺测值的位置返回布尔值
print(x.notnull())
# 返回x中非缺测值的个数
print(x.count())
# 将数据数组x中名为x的维度上的缺测值去除
print(x.dropna(dim="x"))
# 将数据数组x中的缺测值替换为−1
print(x.fillna(-1))
# 将数据数组中的缺测值替换为向前最近的一个非缺测值
print(x.ffill("x"))
# 将数据数组中的缺测值替换为向后最近的一个非缺测值
print(x.bfill("x"))
