'''
import numpy as np

arr = np.arange(4)
print(arr)
print((np.e ** arr).round(2), '\n')

arr2 = np.arange(6).reshape(2, 3)
print(arr2)
print((np.e ** arr2).round(2))

arr3 = np.arange(8).reshape(2, 2, 2)
print(arr3)
print((np.e ** arr3).round(2))
'''

import torch
import numpy as np

arr = torch.arange(4)
print(arr)
print((np.e ** arr).round(decimals=2), '\n')

arr2 = torch.arange(6).reshape(2, 3)
print(arr2)
print((np.e ** arr2).round(decimals=2))

arr3 = torch.arange(8).reshape(2, 2, 2)
print(arr3)
print((np.e ** arr3).round(decimals=2))