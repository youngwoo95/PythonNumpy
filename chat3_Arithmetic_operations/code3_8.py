# 넘파이
'''
import numpy as np

arr = np.arange(4)
#print(f"{arr = }")
#print(3 ** arr, '\n')

arr2 = np.arange(6).reshape(2, 3)
#print(arr2)
#print(2 ** arr2)

arr3 = np.arange(8).reshape(2, 2, 2)
print(arr3)
print(3 ** arr3)
'''

# 파이토치
import torch

arr = torch.arange(4)
print(f"{arr =}")
print(3 ** arr, '\n')

arr2 = torch.arange(6).reshape(2, 3)
print(arr2)
print(2 ** arr2)

arr3 = torch.arange(8).reshape(2, 2, 2)
print(arr3)
print(3 ** arr3)