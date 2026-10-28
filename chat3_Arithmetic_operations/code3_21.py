import numpy as np

u = np.arange(1, 4) # 1 2 3
v = 2 * np.arange(1,4)  # 2 4 6 

M = np.arange(1, 5).reshape(2, 2)
N = 2 * np.arange(1,5).reshape(2,2)

#print(u * v)
#print(np.multiply(u,v))



print(M, '\n')
print(N, '\n')

print(M ** N, '\n')
print(np.power(M, N))