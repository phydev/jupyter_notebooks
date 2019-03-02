import matplotlib.pyplot as plt
import numpy as np


def euler(h):
    lx = 2. * 3.15
    nx = int(lx / h)  # number of points
    f = np.zeros(nx)  # initializing numpy arrays
    g = np.zeros(nx)
    x = np.zeros(nx)
    f_numpy = np.zeros(nx)
    xn = 0.

    # we will integrate the function cos(x)
    # let's save it in an array in order to plot it after the integration
    for i in range(0, nx):
        g[i] = np.cos(xn)
        f_numpy[i] = np.sin(xn)  # this is to test the accuracy of the method
        x[i] = xn
        xn = xn + h

    f[0] = np.sin(0)
    for i in range(0, nx - 1):
        f[i + 1] = f[i] + h * g[i]

    plt.plot(x, f, label='f(x) = sin(x)')
    plt.plot(x, f_numpy, label='NumPy Sin(x)')
    plt.legend()
    plt.show()
    plt.plot(f, g, label='Phase-space')
    plt.legend()
    plt.show()
    return f, x

# plt.plot(x, f, label='f(x) = sin(x)')
# plt.plot(x, f_numpy, label='NumPy Sin(x)')
# plt.legend()
# plt.show()
# plt.plot(f, g, label='Phase-space')
# plt.legend()
# plt.show()
