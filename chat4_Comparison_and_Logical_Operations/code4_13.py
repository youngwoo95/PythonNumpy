import numpy as np
from numpy.random import randint

arr = randint(0, 2, 5).astype(bool)
print(f"arr: {arr}")
print(f"np.logical_not(arr): {np.logical_not(arr)}")


arr2 = randint(0, 2, (3,4)).astype(bool)
print(f"arr2:\n{arr2}\n")
print(f"np.logical_not(arr2): {np.logical_not(arr2)}")