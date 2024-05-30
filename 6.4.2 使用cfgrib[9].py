# 6.4.2  使用cfgrib读取GRIB文件
import xarray as xr

# 将文件路径改为自己的
dataset = xr.open_dataset('fnl_201906011800.grib2',
                          engine='cfgrib',
                          backend_kwargs={
                              'filter_by_keys': {
                                  'typeOfLevel': 'isobaricInhPa'
                              }
                          }
                          )
print(dataset)
print(dataset['u'])
