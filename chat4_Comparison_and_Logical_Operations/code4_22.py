import numpy as np
from numpy.random import randint

n_data = 10
preds = randint(0, 2, n_data)
labels = randint(0, 2, n_data)

print(f"preds: {preds}")
print(f"labels: {labels}\n")


Tps = np.logical_and(preds == True, labels == True).sum()
FPs = np.logical_and(preds == True, labels == False).sum()
FNs = np.logical_and(preds == False, labels == True).sum()
TNs = np.logical_and(preds == False, labels == False).sum()

print(f"{Tps} | {FPs}")
print(f"{FNs} | {TNs}")