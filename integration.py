__author__ = 'lois'
import numpy as np

def simps_method(func_, l_range, u_range, c): # c is the count

    h = (u_range - l_range)/c
    a = func_(l_range) + func_(u_range)
    for i in range(1, c, 2):
        a += 4*func_(l_range+i * h)
    for i in range(2, c-1, 2):
        a += 2*func_(l_range + i * h)
        return a*h/3

if __name__ == "__main__":
    print(simps_method(lambda x: (x**2-1), -2, 2, 10))
    print(simps_method(lambda x: (x**2-1), -2, 2, 10000))
    print(simps_method(lambda x: (1/x), 0.1, 2, 100))


# the midpoint method  is shown below

def midpoint_method(func, l_lim, u_lim, c):

    h = (u_lim - l_lim)/c #this calculates the step length
    x =np.linspace(l_lim, u_lim, c+1)
    s = 0
    midpoints_array = [0]*c
    for i in range(1, c + 1):
        midpoints_array[i-1] = (x[i] + x[i-1])/2
        s += func(midpoints_array[i-1])
    return s*h


if __name__ == "__main__":
    print(midpoint_method(lambda x: (x**2-1), -2, 2, 10))
    print(midpoint_method(lambda x: (x**2-1), -2, 2, 10000))
    print(midpoint_method(lambda x: (1/x), 0.1, 2, 100))
