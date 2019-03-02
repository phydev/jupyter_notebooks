import numpy as np

def check_boundary(x, l):
    if(x>=l): x = x-l
    if(x<0): x = x+l
    return x


def laplacian(f, i, l):
    dx = 1.
    y = i
    yh = check_boundary(i+1, l)
    yl = check_boundary(i-1, l)
    return (f[yh]+f[yl]-2*f[y])/(dx*dx)


def init(l):
    A = np.zeros(l)
    for i in range(0, l):
        A[i] = np.exp(-(i-l/2.)**2/l)
    return A


def integrate(A, dt, final_time):
    time = 0.
    l = len(A)
    while (time < final_time):

        for i in range(0, l):
            A[i] = A[i] + dt * laplacian(A, i, l)

        time += dt

    return A



