import numpy as np

names = ["Fridge", "TV", "Fans", "Light", "Laptop", "Iron"]
watts = np.array([150, 100, 60, 40, 65, 1000])
hours = np.array([24, 5, 8, 6, 4, 1])
kwh = watts * hours / 1000
print(kwh)
print(round(kwh.sum(), 2))
print(kwh.max())
print(kwh.argmax())
print(names[kwh.argmax()])
print(round(kwh.mean(), 2))

heavy = kwh > 1
print(heavy)
print(kwh[heavy])
print(heavy.sum())