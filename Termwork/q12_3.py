n = int(input("Enter the value = "))
sum = 1

while n>0 :
    sum *= (n%10)
    n -= 1

print("Factorial = ",sum)