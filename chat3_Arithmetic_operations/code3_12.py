from numpy.random import uniform

arr = uniform(0, 10, 10)
print(arr, '\n')

arr2 = uniform(0, 10, (10, ))
print(arr2)

arr3 = uniform(0, 10, (2, 3))
print(arr3)

arr4 = uniform(-10, 11, (3, 4))
print(arr4)