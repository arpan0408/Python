# def welcome():
#     '''This f() displays 'Hello BCA Class !' '''
#     print('Hello BCA Class')

# welcome()
# print(help(welcome))

# def welcome(*name):
#     i=0
#     while len(name)>i:
#         print('Hello',name[i])
#         i += 1
# welcome('a','b','c')

# def welcome(fname,lname):
#     print('Hello',fname,lname)
# welcome(lname='Kumar',fname='Arpan')

def welcome(**std):
    print('Hello',std['fname'],std['lname'])
welcome(fname='Arpan',lname='Kumar')
welcome(fname='Santosh',lname='Prasad')
welcome(fname='Garvit',lname='Aggarwal')