n = int(input("Enter the value = "))
sum,tp =  0,n
while tp>0 :
    sum += pow(tp%10,3)
    tp //= 10

if n == sum :
    print(n," is an Armstrong no.")
else :
    print(n," is not an Armstrong no.")
