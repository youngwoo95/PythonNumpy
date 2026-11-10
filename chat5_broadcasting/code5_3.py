import numpy as np
from numpy.random import randint

n_classes, n_subjects = 100, 5
scores = randint(0, 101, (n_classes, n_subjects))
#print(scores.mean(axis=1).round(3))
means = scores.mean(axis=1, keepdims=True)

#print(scores.shape)
#print(means.shape)
scores_ms = scores - means
print(scores_ms.mean(axis=1).round(3))


#means = scores.mean(axis=0, keepdims=True)
#print(scores.shape)
#print(means.shape)
#scores_ms = scores - means

#print(scores_ms.mean(axis=0).round(3))