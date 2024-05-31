import numpy as np

arr = np.arange(24)
print(arr)
arr = arr.reshape(2,4,3)
print(arr)
arr = arr.ravel()
print(arr)