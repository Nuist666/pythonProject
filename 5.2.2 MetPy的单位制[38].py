# MetPy的单位制运算
import numpy as np
from metpy.units import units

distance = np.arange(1, 5) * units.meters
time = units.Quantity(np.arange(1, 5), 'sec')
print(distance / time)
print(3 * units.inch + 5 * units.cm)
print((1 * units.inch).to(units.mm))
