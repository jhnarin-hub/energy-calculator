monthly_kwh = float(input("enter the kwh"))
if monthly_kwh < 100:
    cost = monthly_kwh * 50
elif monthly_kwh >= 100:
    cost = (100 * 50) + (monthly_kwh - 100) * 70
if monthly_kwh >= 200: 
    cost = (100 * 50) + (monthly_kwh - 100) * 90

avg_cost_per_kwH = cost / monthly_kwh
print("Monthly kwH:", round(monthly_kwh, 1))
print("Monthly cost is: N", round(cost, 1), "per month")
print("the average cost per kWh is:N", avg_cost_per_kwH)
