# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y1 = np.e ** x
y2 = np.e ** (-x)

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y1, label="$f(x) = e^x$")
ax.plot(x, y2, label="$f(x) = e^{-x}$")

ax.legend(fontsize=20)

ax.set_title("Exponential Function", fontsize=20)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()
# %%
