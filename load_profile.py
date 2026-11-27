import numpy as np
load = np.zeros(24)
load[:] = 0.3
load[6:8] += 0.5
load[18:23] += 1.0

print(load)
print("total energy is:", load.sum(), "kW")
print("peak load is", load.max(), "kW")
print("peak hour", load.argmax())
print("Average load is:", round(load.mean(), 2), "kWh")
print((load > 1).sum())
print(round(load.sum()* 63, 2))
