import numpy as np

full_scalar = np.full(shape=(), fill_value=5)
full_vector = np.full(shape=(3,), fill_value=np.pi)
full_matrix = np.full(shape=(2, 3), fill_value=np.e)
full_tensor = np.full(shape=(2, 3, 4), fill_value=np.inf)

print(full_scalar)
print(full_vector)
print(full_matrix)
print(full_tensor)