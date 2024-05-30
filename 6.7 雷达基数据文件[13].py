import cinrad

f = cinrad.io.CinradReader('RADA_CHN_DOR_L2_O-Z9551-SA-CAP-20200708032300.bin.bz2')
print(f.available_product(0))
# 读取反射率
tilt_number = 0
data_radius = 230
r = f.get_data(tilt_number, data_radius, 'REF')
print(r)
