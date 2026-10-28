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