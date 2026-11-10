import numpy as np
from numpy.random import uniform

preds = uniform(0, 1, 5).round(3)
labels = uniform(0, 1, 5).round(3)
print(f"preds : {preds}")
print(f"labels : {labels}")

corrects = np.isclose(preds, labels, atol=0.02) 

print(corrects)



'''
[정리]
isClose
- atol
'''