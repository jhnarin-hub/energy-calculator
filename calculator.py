from logging import config


appliance = "tv"
watts = 100
hours = 8
tariff = 60  # naira per kWh, adjust to your band

kwh = watts * hours / 1000
cost = kwh * tariff

print(appliance, "uses", kwh, "kWh per day")
print("Daily cost: N", cost)
