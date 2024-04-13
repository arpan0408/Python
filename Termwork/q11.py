n = int(input("Enter the value = "))
tp = 0

while n>0 :
    tp = (tp*10) + (n%10)
    n //= 10

print("Reversed = ",tp)
