# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)
y = x ** 2

print(f"x:{x}")
print(f"y:{y}")

fig, ax = plt.subplots(figsize=(10, 5))

ax.set_title("$f(x) = x^2$", fontsize=30)
ax.plot(x, y)
ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()

# %%
