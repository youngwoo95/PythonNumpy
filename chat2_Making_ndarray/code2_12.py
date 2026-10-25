import numpy as np

mat1 = np.array([[1,2,3],
                 [4,5,6]])

mat2 = np.array([[1,2],
                 [3,4]])

mat3 = np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])

print(f"{mat1.ndim} / {mat1.shape}")
print(f"{mat2.ndim} / {mat2.shape}")
print(f"{mat3.ndim} / {mat3.shape}")


print(mat1, '\n')
print(mat2, '\n')
print(mat3, '\n')