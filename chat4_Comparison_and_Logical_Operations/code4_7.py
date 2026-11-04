import numpy as np
from numpy.random import randint

M = randint(5, size=(3, 3))
N = randint(5, size=(3, 3))

print(f"M: \n{M}\n")
print(f"N: \n{N}\n")

#print(f"M > N:\n {M > N}\n")
#print(f"np.greater(M,N):\n {np.greater(M,N)}\n")


print(f"M >= N:\n {M >= N}\n")
print(f"np.greater_equal(M,N):\n {np.greater_equal(M,N)}\n")
