import numpy as np
from numpy.random import randint

u = randint(5, size=(5,))
v = randint(5, size=(5,))

print(f"u:{u}")
print(f"v:{v}")

print(f"u == v: {u == v}\n {(u==v).shape}")
print(f"u != v: {u != v}")

print(f"u > v: {u > v}")
print(f"u >= v: {u >= v}")

print(f"u < v: {u < v}")
print(f"u <= v: {u <= v}")