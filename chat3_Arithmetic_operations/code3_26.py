# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y1 = x ** 2
y2 = 2 * (x**2)
y3 = -3 * (x**2) + 10

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y1, label="$f(x) = x^2$")
ax.plot(x, y2, label="$g(x) = 2x^2$")
ax.plot(x, y3, label="$h(x) = -3x^2 + 10$")

ax.legend(fontsize=20)
ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()
# %%
