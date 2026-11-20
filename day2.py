hour = float(input("Enter daily hours of electricity: "))

if hour >= 20:
    print("DEAR CUSTOMER, YOU ARE IN BAND A")
elif hour >= 16:            
    print("DEAR CUSTOMER, YOU ARE IN BAND B")
elif hour >= 12:
    print("DEAR CUSTOMER, YOU ARE IN BAND C")
elif hour >= 8:
    print("DEAR CUSTOMER, YOU ARE IN BAND D")
else:
    print("DEAR CUSTOMER, YOU ARE IN BAND E")
