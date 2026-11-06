from numpy.random import randint

arr = randint(0, 2, 5)
print(f"arr: {arr}")
print(arr.astype(bool))

arr2 = randint(0, 2, (3,4))
print(f"arr2:\n{arr2}\n")
print(arr2.astype(bool))