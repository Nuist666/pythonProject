import numpy as np
lon = np.arange(76.0, 131.5+0.5, 0.5) # np.arange()函数创建的数组不包含参数传入的终点值
lat = np.arange(20.5, 51.5+0.5, 0.5) # 所以在终点值后再加入一个步长以确保最后一个值被包含在结果中
print(lon.shape, lat.shape)
