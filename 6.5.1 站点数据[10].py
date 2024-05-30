# 定义如下读取函数
import numpy as np
import pandas as pd


def grads_sta(path_file, n_sta, n_time):
    dt = np.dtype([('sta', 'S8'), ('lat', 'f4'), ('lon', 'f4'),
                   ('time', 'f4'), ('nlev', 'i4'), ('nflag', 'i4'),
                   ('var', 'f4')])
    df_group = []
    with open(path_file, 'rb') as fid:
        for t in range(n_time):
            data_raw = np.frombuffer(fid.read(n_sta * 32), dtype=dt)
            fid.read(28)
            df = pd.DataFrame(data_raw)
            try:
                df['sta'] = [x.decode() for x in df['sta']]
            except:
                pass
            df_group.append(df)
    return df_group


# 读取示例文件，可参考.ctl描述文件
dat = grads_sta('r160.grd', 160, 1)  # 将文件路径改为自己的
print(dat)
print(type(dat))
