from numpy.random import randint

M = randint(10, size=(2, 3))
N = randint(10, size=(2, 3))

print(M,'\n')
print(N,'\n')

print(M == N, '\n')
print(M != N, '\n')

print(M > N, '\n')
print(M >= N, '\n')

print(M < N, '\n')
print(M <= N, '\n')