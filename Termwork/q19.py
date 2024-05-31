import pandas as pd
import numpy as np

#creating empty series:
s = pd.Series()
print(s,'\n')

#creating a series from an array:
arr = np.array(['A','R','P','A','N'])
s = pd.Series(arr)
print(s,'\n')

#creating series from the array with index:
s = pd.Series(arr,index=[11,12,13,14,15])
print(s)

#creating series from lists:
l = ['A','R','P','A','N']
s = pd.Series(l)
print(s)

#Creating a series from Dictionary: 
d = {5:'A',6:'R',7:'P',8:'A',9:'N'}
s = pd.Series(d)
print(s)

#Creating a series from Scalar value: 
s = pd.Series(21,index=[20,21,22,23,24,25])
print(s)

#label
print(s[0])