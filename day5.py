total_kwh = 0
highest_kwh = 0
highest_name = ""
heavy_count = 0

names = ("Fridge", "TV", "Fan", "Light", "Laptop", "Iron")
watts = (150, 100, 60, 40, 65, 1000)
hours = (24, 5, 8, 6, 4, 1)

for i in range(len(names)):
    kwh = watts[i] * hours[i] / 1000
    total_kwh = total_kwh + kwh
    print(names[i], "uses", kwh, "kwh per day")

    if kwh > 1:
        print(" Warning: High Usage!")
        heavy_count = heavy_count + 1
    if kwh > highest_kwh:
        highest_kwh = kwh
        highest_name = names[i]
percentage_of_biggest_user = highest_kwh / total_kwh * 100
monthly_bill = total_kwh * 63 * 30
print("total daily kWH is;", total_kwh)
print("Heavy appliances:", heavy_count)
print("biggest user:", highest_name, "with", highest_kwh, "kWH per day" ) 
print("percentage of biggest appliance to total kwh is: ", percentage_of_biggest_user)
print("the monthly bill is:N", monthly_bill )

if percentage_of_biggest_user > 50:
    print("please focus on your", highest_name, "consumption")