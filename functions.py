# Some f() of python 

name = "Arpan"

# print(len(name))
# print(type(name))
# print(name.find("a"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())       #convert the all characters in lower case
# print(name.count("a"))        #counting the 'a' in string
# print(name.replace("A","@"))        #replacing 'A' with '@' for temprary
# print(name.isalpha())     #for check the str is alphabatic 
# print(name.isdigit())     #for check the digit on string
# print(name.strip())       #for remove the white spac form string
# print(name*5)       #for print the variable multiple times

# n = "Arpan {}"

# print(n.format(21))

# n1 = 10
# n2 = 20
# n3 = 30

# str = "first-{0} sec-{2} third-{1}"

# print(str.format(n1,n3,n2))


list = ['Arpan','Garvit','Santosh','Ayush']
#Acending order
list.sort()
#Decending order
list.sort(reverse=True)
print(list)

l1 = [1,2,3,4,5,6]
l2 = [100,99,98,97]

# for v in l2:
#     l1.append(v)

l2.sort()
print(l1+l2)

l1.insert(0,'Arpan')
print(l1)



def sum(a,b):
    print(a+b)