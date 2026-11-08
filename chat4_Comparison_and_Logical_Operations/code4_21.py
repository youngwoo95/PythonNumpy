import numpy as np
from numpy.random import randint

n_data = 10
preds = randint(0, 2, n_data)
labels = randint(0, 2, n_data)

print(f"preds: {preds}")
print(f"labels: {labels}\n")

FPs = np.logical_and(preds == True, labels == False)
FNs = np.logical_and(preds == False, labels == True)

print(f"false Positive : {FPs}")
print(f"false Negative : {FNs}")