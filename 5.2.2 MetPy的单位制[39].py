# 转换为国际单位制
from metpy.units import units

Lf = 3.34e6 * units('J/kg')
print(Lf, Lf.to_base_units(), sep='\n')
