band = input("Enter your band (A/B/C/D/E): ").upper()
kwh = float(input("Enter monthly kwh: "))

if band == "A":
    rate = 209.5
elif band == "B":
    rate = 63
elif band == "C":
    rate = 50
elif band == "D":
    rate = 50
elif band == "E":
    rate = 50
else:
    rate = 0

if band not in {"A", "B", "C", "D", "E"}:
    print("Invalid band")
else:
    cost = kwh * rate

    print("Rate: N", rate, "per kwh")
    print("Monthly cost: N", cost)

    if cost > 20000:
        print("High electricity cost, consider solar")