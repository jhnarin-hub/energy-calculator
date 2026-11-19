tarrif = 60 #naira per kwh
fridge_kwh = 150 * 24 / 1000
tv_kwh = 100 * 5 / 1000
light_kwh = 40 * 6 / 1000
fan_kwh = 150 * 10 / 1000
total_kwh = fridge_kwh + tv_kwh + light_kwh + fan_kwh
total_cost = total_kwh * tarrif
print ("fridge:", fridge_kwh, "kwh" )
print ("tv:", tv_kwh, "kwh")
print ("light:", light_kwh, "kwh")
print ("fan:", fan_kwh, "kwh")
print ("total kwh:", total_kwh, "kwh")
print ("total cost :N", total_cost)
print ("monthly cost:N", total_cost*31)


