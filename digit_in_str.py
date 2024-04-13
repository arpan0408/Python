str = input("Enter the value : ")
count = 0
for i in range(len(str)):
    if(str[i].isdigit()):
        print(str[i])
        count += 1

print("Total",count)