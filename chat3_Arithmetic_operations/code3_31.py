# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 100)
numerator = np.e ** x - np.e**(-x)
denominator = np.e**x + np.e**(-x)
y = numerator / denominator

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, zorder=3)


ax.legend(fontsize=20)

ax.set_title("Tanh Function", fontsize=20)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()
# %%
import torch
import matplotlib.pyplot as plt

x = torch.linspace(-10, 10, 100)
numerator = np.e ** x - np.e**(-x)
denominator = np.e**x + np.e**(-x)
y = numerator / denominator

fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(x, y, zorder=3)


ax.legend(fontsize=20)

ax.set_title("Tanh Function", fontsize=20)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()