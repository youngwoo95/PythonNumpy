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