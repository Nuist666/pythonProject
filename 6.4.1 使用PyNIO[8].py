# 使用PyNIO读取GRIB文件,来源于NCL，不支持Windows
import xarray as xr

dataset = xr.open_dataset('fnl_201906011800.grib2', engine='pynio')  # 将文件路径改为自己的
print(dataset)
data = dataset['TMP_P0_L1_GLL0']
print(data)
