import numpy as np


a, b = np.array(10), np.array(3)


#print(dir(a))
print(f"{a + b =} / {a.__add__(b) =}")
print(f"{a - b =} / {a.__sub__(b) =}")
print(f"{a * b =} / {a.__mul__(b) =}")
print(f"{a ** b =} / {a.__pow__(b) =}")
print(f"{a / b =} / {a.__truediv__(b) =}")
print(f"{a // b =} / {a.__floordiv__(b ) =}")
print(f"{a % b =} / {a.__mod__(b) =}")