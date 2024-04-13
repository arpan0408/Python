str=input("enter first string" )
str1=input("enter second string")
if(len(str)!=len(str1)):
    print("it is not a anagram")
else:
    l1=list(str)
    l2=list(str1)
    l1.sort()
    l2.sort()
    if(l1==l2):
        print("it is an anagram")
    else:
        print("it is not anagram")