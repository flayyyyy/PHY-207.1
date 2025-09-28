import numpy as np
import matplotlib.pyplot as plt

def wick(beta, ax):
    theta = np.arctan(beta)
    ax.arrow(0,0,1,0,head_width=0.05,fc='k',ec='k')
    ax.arrow(0,0,0,1,head_width=0.05,fc='k',ec='k')
    ax.text(1.05,0,"x",fontsize=12)
    ax.text(0,1.05,"ict",fontsize=12)
    x_axis = np.array([np.cos(theta), np.sin(theta)])
    t_axis = np.array([-np.sin(theta), np.cos(theta)])
    ax.arrow(0,0,x_axis[0],x_axis[1],head_width=0.05,color='r')
    ax.arrow(0,0,t_axis[0],t_axis[1],head_width=0.05,color='b')
    ax.text(x_axis[0]*1.1, x_axis[1]*1.1,"x'",color='r')
    ax.text(t_axis[0]*1.1, t_axis[1]*1.1,"ict'",color='b')
    ax.set_aspect('equal')
    ax.set_xlim(-1.2,1.2)
    ax.set_ylim(-1.2,1.2)
    ax.xaxis.set_ticks(np.arange(-1.0, 1.25, 0.25))
    ax.yaxis.set_ticks(np.arange(-1.0, 1.25, 0.25))
    ax.set_title(f"V = {beta} c, rotation angle θ ≈ {np.degrees(theta):.1f}°")
    ax.grid(True)

fig, axes = plt.subplots(1,3,figsize=(15,5))
wick(0.01, axes[0])
wick(0.5, axes[1])
wick(0.9999, axes[2])
plt.tight_layout()
plt.show()


def lorentz(beta, ax):
    t = np.linspace(-1, 1, 200)
    x_tprime = beta*t
    ax.plot(x_tprime, t, 'b', label="ct'-axis")
    x = np.linspace(-1, 1, 200)
    t_xprime = beta*x
    ax.plot(x, t_xprime, 'r', label="x'-axis")
    ax.axhline(0, color='k', linewidth=1)
    ax.axvline(0, color='k', linewidth=1)
    ax.plot(t, t, 'k--', alpha=0.5)
    ax.plot(-t, t, 'k--', alpha=0.5)
    ax.set_title(f"V = {beta}c")
    ax.set_xlabel("x")
    ax.set_ylabel("ct")
    ax.set_xlim(-1,1)
    ax.set_ylim(-1,1)
    ax.legend()
    ax.grid(True)

fig, axes = plt.subplots(1,3,figsize=(15,5))
lorentz(0.01, axes[0])
lorentz(0.5, axes[1])
lorentz(0.9999, axes[2])
plt.tight_layout()
plt.show()
