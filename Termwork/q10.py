n = int(input("Enter the value = "))
tp,flg = n-1,0

while tp>1:
    if n%tp == 0:
        flg = 1
    tp -= 1

if flg == 1 :
    print(n," is not a Prime no.")

else :
    print(n," is a Prime no.")