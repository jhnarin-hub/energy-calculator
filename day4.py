names = ("fridge", "tv", "fan", "light", "laptop", "iron")
watt = (150, 100, 60, 40, 65, 1000)
hours = (24, 5, 8, 6, 4, 1)
total_kwh = 0
for i in range(len(names)):
    kwh = watt[i] * hours[i] / 1000
    if watt[i] > 100:
         print(names[i], "is higher than 100 watts")
    total_kwh = total_kwh + kwh
    monthly_kwh = total_kwh * 30
    cost = monthly_kwh * 65
    print(i, names[i], kwh, "kwh")
print("total kwh:", total_kwh, "kwh")
print("monthly kwh:", monthly_kwh, "kwh")
print("monthly cost: N", cost, "for a band b customer")