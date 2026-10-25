import numpy as np

empty_scalar = np.empty(shape=())
empty_vector = np.empty(shape=(3,))
empty_matrix = np.empty(shape=(2,3))
empty_tensor = np.empty(shape=(2, 3, 4))

print(empty_scalar)
print(empty_vector)
print(empty_matrix)
print(empty_tensor)