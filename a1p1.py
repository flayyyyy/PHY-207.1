import numpy as np
import matplotlib.pyplot as plt

V = np.linspace(0,0.9999,500)
c = 1.0
v_gp = c + V
v_gm = c - V
v_l = c+V-V

plt.figure(figsize=(7,5))
plt.plot(V, v_gp, 'r--', label="Galilean: c+V")
plt.plot(V, v_gm, 'b--', label="Galilean: c−V")
plt.plot(V, v_l, 'k', label="Lorentz: c (invariant)")
plt.xlabel("V/c")
plt.ylabel("Measured light speed (units of c)")
plt.title("Galilean vs Lorentz Predictions for Light Speed")
plt.legend()
plt.grid(True)
plt.show()
