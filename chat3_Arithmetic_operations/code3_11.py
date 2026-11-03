# 넘파이
'''
import numpy as np
from numpy.random import randint

arr = randint(0, 10, 10)
print(arr, '\n')

arr2 = randint(0, 10, (10, ))
print(arr2)

arr3 = randint(0, 10, (2, 3))
print(arr3)

arr4 = randint(-10, 11, (3, 4))
print(arr4)
'''

# 파이토치
import torch

arr = torch.randint(0, 10, (10,))
print(arr, '\n')

arr2 = torch.randint(0, 10, (2,3))
print(arr2)

arr3 = torch.randint(-10, 11, (3, 4))
print(arr3)

'''
torch.randint는 크기를 꼭 튜플로 줘야 한다.
'''