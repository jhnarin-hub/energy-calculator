#energy calculator v2
# calculates a household's daily and monthly energy use and cost

#data for the appliances
names = ["fridge", "TV", "Fan", "Lights", "Laptop", "Iron"]
watts = [150, 100, 60, 40, 65, 1000]
hours = [24, 5, 8, 6, 4, 1]

#---- starting values (must be set before the loop)
total_kwh = 0
highest_kwh = 0
highest_name = ""
heavy_count = 0

#----- go through every appliances using the loop
for i in range(len(names)):
    kwh = watts[i] * hours[i] / 1000
    total_kwh = total_kwh + kwh
    print(names[i], "consumes", round(kwh, 2), "kWh a day")

    #flag heavy user
    if kwh > 1:
        print("warning!, high consumption")
        heavy_count = heavy_count + 1
    #track the biggest user
    if kwh > highest_kwh:
        highest_kwh = kwh
        highest_name = names[i]

    #summary (runs once, after the loop)
    percentage = round(highest_kwh / total_kwh * 100)
    monthly_kwh = total_kwh * 30

    #tiered tarrff: first 100kwh at 50, while the rest at 70
if monthly_kwh <= 100:
    cost = monthly_kwh * 50
else:
    cost = (100 * 50) + (monthly_kwh - 100) * 70

print("-------------")
print("Total daily kwh is:", total_kwh, "kWh")
print("Heavy appliances:", heavy_count)
print("Biggest user:", highest_name, "-", percentage, "% of total")
print("monthly kWh:", monthly_kwh, "kWh")
print("Monthly cost: N", round(cost, 2))