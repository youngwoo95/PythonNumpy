# 넘파이
'''
import numpy as np

arr1 = np.arange(8).reshape(2, 4)
print(arr1)

arr2 = np.arange(12).reshape(3, 4)
print(arr2)

arr3 = np.arange(24).reshape(2, 3, 4)
print(arr3.ndim, arr3.shape)
'''

# 파이토치
import torch
arr1 = torch.arange(8).reshape(2, 4)
print(arr1)

arr2 = torch.arange(12).reshape(3,4)
print(arr2)

arr3 = torch.arange(24).reshape(2, 3, 4)
print(arr3.ndim, arr3.shape)