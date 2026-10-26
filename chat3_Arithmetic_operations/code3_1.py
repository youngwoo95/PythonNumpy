import numpy as np

arr = np.arange(8)
print(arr)
print(arr.reshape(4,2))

print(arr.reshape(2, 4))

arr = np.arange(12)
print(arr)
print(arr.ndim, arr.shape)

print(arr.reshape(3, 4))
print(arr.ndim, arr.shape) # 원본은 바뀌지 않음.

print(arr.reshape(4,3))