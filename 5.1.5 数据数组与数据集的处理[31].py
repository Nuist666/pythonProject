# 数据集和数据数组的转换
import xarray as xr

ds = xr.Dataset({"foo": (("x", "y", "z"), [[[42]]]), "bar": (("y", "z"), [[24]])})
print(ds.to_array())
ds = xr.Dataset({"foo": (("x", "y", "z"), [[[42]]]), "bar": (("y", "z"), [[24]])})
arr = ds.to_array()
print(arr.to_dataset(dim="variable"))
