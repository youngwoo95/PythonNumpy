import numpy as np
from numpy.random import randint

n_data = 10
preds = randint(0, 2, n_data)
labels = randint(0, 2, n_data)

print(f"preds: {preds}")
print(f"labels: {labels}\n")


TP = np.logical_and(preds == True, labels == True).sum()
FP = np.logical_and(preds == True, labels == False).sum()
FN = np.logical_and(preds == False, labels == True).sum()
TN = np.logical_and(preds == False, labels == False).sum()


acc = (TP + TN) / (TP + FP + TN + FN)
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1score = (2 * precision * recall) / (precision + recall)


print(f"{acc = }")
print(f"{precision = }")
print(f"{recall = }")
print(f"{f1score = }")

