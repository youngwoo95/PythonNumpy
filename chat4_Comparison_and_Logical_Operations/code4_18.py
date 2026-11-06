import numpy as np
from numpy.random import uniform

preds = uniform(0, 0.5, 3).round(3)
labels = uniform(0, 0.5, 3).round(3)
print(f"preds : {preds}")
print(f"labels : {labels}")

corrects = np.isclose(preds, labels, atol=0.02) 
print(f"corrects: {corrects}\n")

all_corrects = np.allclose(preds, labels, atol=0.2)
all_corrects_ = np.all(np.isclose(preds, labels, atol=0.02))
print(f"all_corrects: {all_corrects}\n")
print(f"all_corrects_: {all_corrects_}\n")




'''
[정리]
isClose
- atol
'''