# 定义如下读取函数
import numpy as np
import xarray as xr
import pandas as pd


def grads_grid(path_file, nx, ny, nt,
               lon_0, lon_step, lat_0, lat_step,
               t_0, t_freq, var_list, z_list):
    data_raw = np.fromfile(path_file, dtype=np.float32)
    n_var = len(var_list)
    nz = len(z_list)
    data_raw = data_raw.reshape((nt, n_var, nz, ny, nx))
    time_list = pd.date_range(t_0, periods=nt, freq=t_freq)
    lon = np.arange(lon_0, lon_0 + lon_step * nx, lon_step)
    lat = np.arange(lat_0, lat_0 + lat_step * ny, lat_step)
    data = xr.DataArray(data_raw,
                        coords=[time_list, var_list, z_list, lat, lon],
                        dims=['time', 'var', 'level', 'lat', 'lon']
                        ).to_dataset('var')
    return data


# 读取示例文件，可参考.ctl描述文件
dataset = grads_grid('hgt500.grd',
                     nx=144, ny=73, nt=732,
                     lon_0=0, lon_step=2.5, lat_0=-90, lat_step=2.5,
                     t_0='1948-01-01', t_freq='1M', var_list=['hgt'],
                     z_list=[500])
print(dataset)
