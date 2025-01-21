units=int(input("Enter units consumed:"))
if units<=50:
    print("INR 3/unit")
elif 51<=units<=150:
    print("INR 5/unit")
else:
    print("INR 8/unit")