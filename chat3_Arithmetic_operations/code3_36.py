import numpy as np
from numpy.random import uniform

n_classes = 5
preds = uniform(-2, 2, n_classes)

print(preds)

numerators = np.e ** preds
denominator = numerators.sum()
softmax = numerators / denominator


print(numerators)
print(denominator)
print(softmax)