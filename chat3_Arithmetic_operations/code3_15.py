# 넘파이
'''
import numpy as np

arr = np.arange(-5, 6)
#print(dir(arr))
print(np.negative(arr))
print(arr.__neg__())
print(-arr)

#print(np.negative(arr))
#print(arr.__neg__())
#print(-arr)

arr2 = np.arange(6).reshape(2, 3)
print(np.negative(arr2))
print(arr2.__neg__())
print(-arr2)
'''

# 파이토치
import torch

arr = torch.arange(-5, 6)
print(dir(arr))
print(torch.negative(arr))
print(arr.__neg__())
print(-arr)

arr2 = torch.arange(6).reshape(2, 3)
print(torch.negative(arr2))
print(arr2.__neg__())
print(-arr2)