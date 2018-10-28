import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-6, 6, 20)
y = x**2 + 2*x

fig, axes = plt.subplots(nrows=1, ncols=2)

axes[0].plot(x, y, label="X vs Y")
axes[0].plot(y, x, label="Y vs X")


axes[0].set_title("First axes")
axes[1].set_title("Second axes")

axes[0].legend()

plt.tight_layout

plt.show()
