n = int(input("Enter the value = "))
count = 0

if n==9 :
    print("You get the value in 1 attempt.")
else :
    while n!=9 :
        n = int(input("Try another value = "))
        count += 1
    print("You get the value in ",count," attempts.")