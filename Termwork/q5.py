cost = int(input("Enter the cost price of mobile = "))

if cost < 50000 :
    print("GST = ",cost*.1)
    print("Total price = ",(cost*.1)+cost)

elif cost > 50000 and cost <= 100000:
    print("GST = ",cost*.15)
    print("Total price = ",(cost*.15)+cost)

elif cost > 100000:
    print("GST = ",cost*.18)
    print("Total price = ",(cost*.18)+cost)