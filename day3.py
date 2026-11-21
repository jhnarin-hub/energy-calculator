appliances = ["fridge", "TV", "Fan", "Lights", "Laptop", "Iron"]
watts = [150, 100, 60, 40, 65, 1000]
hours = [24, 5, 8, 6, 4, 1]
print(appliances[0], "uses", watts[0], "watts for", hours[0], "hours")
print(appliances[5], "uses", watts[5], "watts for", hours[5], "hours")

kwh = watts[0] * hours[0] / 1000
print(appliances[0], "uses", kwh, "kWh per day")
appliances.append("microwave")
watts.append(1200)
hours.append(2)
print(len(appliances))
print(appliances[0], appliances[-1])
print(watts[2] + watts[3])
name = (input("enter your name:"))
print("Hello", name, "thank you for visiting us")
