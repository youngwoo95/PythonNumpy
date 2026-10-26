# %%

import numpy as np
import matplotlib.pyplot as plt

#x = np.arange(-3, 4)
x = np.linspace(-5, 3, 100)
y = x**2

fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(x, y)
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()

# %%
