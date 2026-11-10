import numpy as np

A = np.arange(3).reshape(3, 1)
B = (np.arange(4)+10).reshape(1, 4)

print(f"A: {A.shape}\n{A}\n")
print(f"B: {B.shape}\n{B}\n")

C = A + B
print(f"A + B: {C.shape}\n{C}\n")