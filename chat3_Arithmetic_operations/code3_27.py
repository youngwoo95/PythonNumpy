# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = (x ** 2) + 2*x


fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, label="$f(x) = x^2 + 2x$")

ax.legend(fontsize=20)
ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()
# %%
