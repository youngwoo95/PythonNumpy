import numpy as np

tensor = np.array([[[1., 2.],
                    [3., 4.]],

                    [[5., 6.],
                     [7., 8.]]])

print(np.zeros_like(tensor))
print(np.ones_like(tensor))
print(np.empty_like(tensor))
print(np.full_like(tensor, fill_value=np.pi))
