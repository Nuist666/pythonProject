# 读取WRF-ARW输出文件
import xarray as xr
import wrf
from netCDF4 import Dataset

# 将文件路径改为自己的
ncfile = Dataset('wrfout_d01_2017-08-10_000000.nc')
p = wrf.getvar(ncfile, 'pressure', timeidx=wrf.ALL_TIMES)  # 对于getvar()函数，可以指定timeidx参数的值为整数以选择提取时次，例如timeidx=0
rh = wrf.getvar(ncfile, 'rh', timeidx=wrf.ALL_TIMES)  # timeidx=wrf.ALL_TIMES表明提取全部时次
print(rh)
# 将数据插值到等压面
rh_500 = wrf.interplevel(rh, p, 500)  # interplevel()函数支持同时插值到多个等压面
rh_850_to_500 = wrf.interplevel(rh, p, [850, 700, 500])
print(rh_850_to_500)
