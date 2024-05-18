# 使用带有单位的变量进行MetPy中的函数计算
import numpy as np
import metpy.calc as mpcalc
from metpy.units import units

temperature = 73.2 * units("degF")  # 通过unit()函数传入单位字符串，当单位字符串包含空格及符号时只能用此方法
rh = 64 * units.percent  # 通过units.xxx赋单位
dewpoint = mpcalc.dewpoint_from_relative_humidity(temperature, rh)
print(dewpoint)
