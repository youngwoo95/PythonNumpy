#%%
import numpy as np
from numpy.random import uniform

n_data = 5
preds = uniform(-10, 10, n_data).round(2)
labels = uniform(-10, 10, n_data).round(2)

print(f"preds: {preds}")
print(f"labels: {labels}")


abs_errors = np.abs(preds - labels)
#squared_errors = np.power(preds - labels, 2)

mse = abs_errors.mean()

print(f"abs_errors: {abs_errors}")
print(f"mse: {mse}")

# %%
