# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = 3 * (x**3) + 2 * (x**2) + x - 10


fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, label="$f(x) = 3x^3 + 2x^2 + x - 10$")
ax.legend(fontsize=20)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()
# %%
