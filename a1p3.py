import numpy as np
import matplotlib.pyplot as plt

beta = np.linspace(0, 0.9999, 500)
gamma = 1 / np.sqrt(1 - beta**2)
plt.figure(figsize=(8,5))
plt.plot(beta, gamma, label=r'$\tau / \tau_0 = \gamma$')
for v in [0.01, 0.5, 0.9999]:
    g = 1/np.sqrt(1-v**2)
    plt.scatter(v, g, color="red")
    plt.text(v, g+2, f"V={v}c")
plt.ylim(0,80)
plt.xlabel("V/c")
plt.ylabel(r"$\tau / \tau_0$")
plt.title("Lifetime of the particle")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
