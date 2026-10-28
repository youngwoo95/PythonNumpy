# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y1 = x ** 2
y2 = 2 * (x**2)

fig, ax = plt.subplots(figsize=(10, 5))

ax.set_title("$f(x) = x^2$", fontsize=30)
ax.plot(x, y1, label=f"$f(x) = x^2$")
ax.plot(x, y2, label=f"$g(x) = 2x^2$")
ax.legend(fontsize=20)
ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()
# %%
