import numpy as np
import math as mt
import matplotlib.pyplot as plt


def metEiLer(f, x0, y0, xn, h):
    x = []
    y = []
    x.append(x0)
    y.append(y0)
    h = min(h, xn - x0)
    while x0 < xn:
        x0 += h
        y0 += h * f(x0, y0)
        x.append(x0)
        y.append(y0)
    return np.array(x), np.array(y)


def f(x, y):
    return mt.cos(x) + 4 * y


def f_res(x):
    return (1 / 17) * (21 * mt.exp(4 * x) + mt.sin(x) - 4 * mt.cos(x))


xnew, ynew = metEiLer(f, 0, 1, 1, 0.1)
yres = [f_res(i) for i in xnew]
err = [mt.fabs(f_res(xnew[k] - ynew[k])) for k in range(len(xnew))]

for j in range(len(xnew)):
    print("%.1f %.3f %.4f" % (xnew[j], ynew[j], err[j]))

plt.plot(xnew, ynew, "o", label="metEiLer", color="k")
xres = np.linspace(np.min(xnew), np.max(xnew), 100)
yres2 = [f_res(i) for i in xres]
plt.plot(xres, yres2, lw=2, color="k", label="analytical solution")
plt.grid(True)
plt.legend()
plt.show()
