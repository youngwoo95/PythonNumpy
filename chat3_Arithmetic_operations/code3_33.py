# %%
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y_true = np.cos(x)

y1 = np.ones_like(x) # (100, )
y2 = y1 - (x**2) / factorial(2)
y3 = y2 + (x**4) / factorial(4)
y4 = y3 - (x**6) / factorial(6)
y5 = y4 + (x**8) / factorial(8)
y6 = y5 - (x**10) / factorial(10)

fig, ax = plt.subplots(figsize=(10, 10))
ax.plot(x, y_true, color='black', zorder=10)
#ax.plot(x, y1, label=f"1st")
#ax.plot(x, y2, label=f"2st")
#ax.plot(x, y3, label=f"3st")
#ax.plot(x, y4, label=f"4st")
#ax.plot(x, y5, label=f"5st")
#ax.plot(x, y6, label=f"6st")

for graph_idx, y in enumerate([y1, y2, y3, y4, y5, y6]):
    ax.plot(x, y, label=f"{graph_idx + 1}st")

ax.legend(fontsize=20)

ax.set_title("Taylor Approximation of Cos", fontsize=20)

ax.axhline(y=0, color='gray')
ax.axvline(x=0, color='gray')
ax.grid()
ax.set_ylim([-2, 2])
ax.tick_params(labelsize=20)
fig.tight_layout()
plt.show()
# %%
