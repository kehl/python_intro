__author__ = 'lois'
import numpy as np

def simpson(f, a, b, n):
    delta = (b - a)/n
    x = np.linspace(a, b, n + 1)
    s= 0
    for i in range(0, n, 2):
        s += f(x[i]) + 4*f(x[i + 1]) + f(x[i+2])
    return (delta/3)*s
if __name__ == "__main__":
    print("For Simpson, Integral of x^2-1 from -2 to 2 is: ",simpson(lambda x: (x**2 - 1), -2, 2, 10))
    print("For Simpson, Integral of x^2-1 from -2 to 2 is: ",simpson(lambda x: (x**2-1), -2, 2, 10000))
    print("For Simpson, Integral of x^2-1 from -2 to 2 is: ",simpson(lambda x: (1/x), 0.1, 2, 100))

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