n = int(input("Enter the value : "))
# fact = 1
# for i in range(n,1,-1):
#     fact *= i
# print(fact)

def fact(n):
    if(n<=1):
        return 1
    else:
        return n*fact(n-1)

print(fact(n))