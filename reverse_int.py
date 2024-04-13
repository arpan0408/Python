#Reverse the int value 

n = int(input("\nEnter the value : "))
tp = 0

while n>0 :
    tp = (tp*10) + (n%10)
    n = n//10

print("\nResult : ",tp)