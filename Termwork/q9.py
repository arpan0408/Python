n1 = int(input("Enter the 1st number = "))
n2 = int(input("Enter the 2nd number = "))
tp1,tp2 = n1+1,n2
print("With including both numbers : ")
while n1<=n2 :
    if n1%2 == 0:
        print(n1)

    n1 += 1

print("Without including both numbers : ")
while tp1<tp2 :
    if tp1%2 == 0:
        print(tp1)
    tp1 += 1