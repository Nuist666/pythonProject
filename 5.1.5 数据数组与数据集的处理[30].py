# 数据的变形和重组
import xarray as xr

ds = xr.Dataset({"foo": (("x", "y", "z"), [[[42]]]), "bar": (("y", "z"), [[24]])})
# 使用transpose("y", "z", "x")调整其维度
print(ds.transpose("y", "z", "x"))
# 当不传入参数时，则默认逆转全部维度顺序
print(ds.transpose())
# 扩充和删除维度
expanded = ds.expand_dims("w")
print(expanded)
print(expanded.squeeze("w"))
