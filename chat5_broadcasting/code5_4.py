import numpy as np

A = np.arange(3).reshape(1, 3)
B = (np.arange(9)+10).reshape(3, 3)

print(f"A: {A.shape}\n{A}\n")
print(f"B: {B.shape}\n{B}\n")

C = A + B
print(f"A + B: {C.shape}\n{C}\n")

