# 偏移量单位
from metpy.units import units

Lf = 3.34e6 * units('J/kg')
print(Lf, Lf.to_base_units(), sep='\n')
print(25 * units.degC + 5 * units.delta_degC)
print(273 * units.kelvin + 10 * units.kelvin)
