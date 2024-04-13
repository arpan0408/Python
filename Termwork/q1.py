#creating differnet datatype variables
str = 'Arpan'
n = 21
list = [1,2,3,4,5]
tuple = (6,7,8,9)
set = {8,5,2,6}
dict = {1:"Arpan",2:21,3:'E',4:True}

#printing the values of list
for l in list:
    print(l)

#printing the values of tuple
for t in tuple:
    print(t)

#printing the values of set
for s in set:
    print(s)

#printing the values of dict
for d in dict.items():
    print(d)

#deleting values from variables
print("Deleted value from list = ",list.pop(3))
print("Deleted value from set = ",set.pop())
print("Deleted value from dictionary = ",dict.pop(3))



