# str=input("enter first string" )
# str1=input("enter second string")
# if(len(str)!=len(str1)):
#     print("it is not a anagram")
# else:
#     l1=list(str)
#     l2=list(str1)
#     l1.sort()
#     l2.sort()
#     if(l1==l2):
#         print("it is an anagram")
#     else:
#         print("it is not anagram")

str = 'Hello World moon '
l = str.rstrip(" ").split(' ')
print(len(l[len(l)-1]))
# if(l[len(l)-1]!=' '):
#     print(len(l[len(l)-1]))
# else:
#     print(len(l[len(l)-2]))