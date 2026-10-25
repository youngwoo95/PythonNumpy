import numpy as np

mat = np.array([[10., 20., 30.],
                [40., 50., 60.]])

print(np.zeros_like(mat))
print(np.ones_like(mat))
print(np.empty_like(mat))
print(np.full_like(mat, fill_value=np.pi))