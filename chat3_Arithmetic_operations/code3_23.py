import numpy as np
from numpy.random import randint

u = randint(1, 10, 4) # 1 2 3
v = randint(1, 10, 4)  # 2 4 6 

M = randint(1, 10, (2,2))
N = randint(1, 10, (2,2))

#print(u * v)
#print(np.multiply(u,v))


#print(u, '\n')
#print(v, '\n')
#print(u % v, '\n')
#print(np.remainder(u, v))


print(M, '\n')
print(N, '\n')
print(M % N, '\n')
print(np.remainder(M, N))