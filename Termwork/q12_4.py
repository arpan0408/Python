n = int(input("Enter the value = "))
flg,tp = 0,n

while tp>0 :
    flg = (flg*10) + (tp%10)
    tp //= 10

if flg == n:
    print(n," is a Palindrome no.")
else :
    print(n," is not a Palindrome no.")