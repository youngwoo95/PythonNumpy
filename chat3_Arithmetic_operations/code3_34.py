#%%
import numpy as np
from numpy.random import uniform

n_data = 5
preds = uniform(-10, 10, n_data).round(2)
labels = uniform(-10, 10, n_data).round(2)

print(f"preds: {preds}")
print(f"labels: {labels}")


squared_errors = (preds - labels) ** 2
#squared_errors = np.power(preds - labels, 2)

mse = squared_errors.mean()

print(f"squared_errors: {squared_errors}")
print(f"mse: {mse}")

# %%
