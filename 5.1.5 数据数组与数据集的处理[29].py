# 数据的拆分与组合
import xarray as xr
import numpy as np

ds = xr.Dataset({"foo": (("x", "y"), np.random.rand(4, 3))},
                coords={"x": [10, 20, 30, 40], "letters": ("x", list("abba"))})
arr = ds["foo"]
print(ds)
# 按数据集中变量或坐标的名称进行分组
print(ds.groupby("letters"))
# 使用.groups属性查看组索引
print(ds.groupby("letters").groups)
# 对每个分组进行函数运算
print(ds["foo"].groupby("letters").mean(dim="x"))
