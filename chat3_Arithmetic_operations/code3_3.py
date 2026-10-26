import numpy as np

arr1 = np.arange(8).reshape(2, 4)
print(arr1)

arr2 = np.arange(12).reshape(3, 4)
print(arr2)

arr3 = np.arange(24).reshape(2, 3, 4)
print(arr3.ndim, arr3.shape)