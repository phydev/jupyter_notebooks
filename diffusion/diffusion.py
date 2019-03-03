import numpy as np

def check_boundary(x, l):
    """
     this function apply periodic boundary conditions for x.

     x (real) : verify if x is between the simulation domain
     l (real) : boundary of the simulation box
    :return:
    """
    if(x>=l): x = x-l
    if(x<0): x = x+l
    return x


def laplacian(f, i, l):
    """
        this function calculates the laplacian of f[i]

    f (array) : array containing the function values we are integrating
    i (integer) : position
    l (integer) : boundary of the simulation box
    return : returns the laplacian
    """
    dx = 1.
    y = i
    yh = check_boundary(i+1, l)
    yl = check_boundary(i-1, l)
    return (f[yh]+f[yl]-2*f[y])/(dx*dx)


def init(l):
    """
        this function takes the length l and returns an
        array A with a gaussian distribution

    l (integer)
    return: array A with gaussian distribution
    """
    A = np.zeros(l)
    for i in range(0, l):
        A[i] = np.exp(-(i-l/2.)**2/l)
    return A


def integrate(A, dt, final_time):
    """
        takes the array A and integrate it for final_time steps
        using Euler's method and time step dt.

    A (array) :
    dt (real) :
    final_time (real) :
    return : result of the integration A (array)
    """
    time = 0.
    l = len(A)
    while (time < final_time):

        for i in range(0, l):
            A[i] = A[i] + dt * laplacian(A, i, l)

        time += dt

    return A



