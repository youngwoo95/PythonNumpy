import numpy as np
from numpy.random import randint

arr1 = randint(0, 2, 5).astype(bool)
arr2 = randint(0, 2, 5).astype(bool)

print(f"arr1: {arr1}")
print(f"arr2: {arr2}")

print(f"xor: {np.logical_xor(arr1, arr2)}")



#arr1 = randint(0, 2, (2,3)).astype(bool)
#arr2 = randint(0, 2, (2,3)).astype(bool)


#print(f"arr1: \n{arr1}\n")
#print(f"arr2: \n{arr2}\n")

#print(f"and: \n{np.logical_and(arr1, arr2)}")
#print(f"or: \n{np.logical_or(arr1, arr2)}")
