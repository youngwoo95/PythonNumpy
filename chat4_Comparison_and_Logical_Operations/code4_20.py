import numpy as np
from numpy.random import randint

n_data = 10
preds = randint(0, 2, n_data)
labels = randint(0, 2, n_data)

print(f"preds: {preds}")
print(f"labels: {labels}\n")


print(preds == 1)
print(labels == 1)

Tps = np.logical_and(preds == True, labels == True)
TNs = np.logical_and(preds == False, labels == False)

print(f"True Positive: {Tps}") 
print(f"True Negative: {TNs}") 
