str = input("Enter the value : ")
f = False
for i in range(len(str)-1):
    if(str[i].lower() == 'e' and str[i+1].lower() == 'l'):
        new = str.upper()
        f = True
        break
    
if (f == False):
    print("The substring does not exist.")

else:
    print(new)