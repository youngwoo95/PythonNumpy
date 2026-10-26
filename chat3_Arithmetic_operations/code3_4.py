import numpy as np

arr = np.arange(4)
print(arr)
print(10 + arr)

arr2 = np.arange(6).reshape(2,3)
print(arr2)
print(arr2 + 10, '\n')

arr3 = np.arange(8).reshape(2, 2, 2)
print(arr3)
print(10 + arr3)