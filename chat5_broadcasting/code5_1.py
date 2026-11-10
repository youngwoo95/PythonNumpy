import numpy as np

A = np.arange(12).reshape(4, 3)
B = (np.arange(3) + 10).reshape(1, 3)

print(f"A: {A.shape}\n{A}\n")
print(f"B: {B.shape}\n{B}\n")

C = A - B
print(f"A + B : {C.shape}\n{C}")