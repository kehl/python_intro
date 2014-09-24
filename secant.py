__author__ = 'lois'

from numpy import *
from math import*
"""
def sec_method (f, a0 ,b0 , error):

    x0=a0
    x1=b0
    i=0
    n=100
    while i in range(n):
        x2=x1-(f(x1)*(x1-x0))/(f(x1)-f(x0))
        if abs(f(x2)) < error and abs(x2-x1) < error:
            return x2
        elif f(x1) == f(x0):
            break
        else:
            x0 = x1
            x1 = x2
        return x2

if __name__ == "__main__":
    print(sec_method(lambda x: sin(x)+cos(x), pi/2, 3*(pi/2), 1e-6))
    print(sec_method(lambda x: sin(x)+cos(x), -pi/2, pi/2, 1e-6))
    print(sec_method(lambda x: (x**3), 5, 6, 1e-9))
"""
def secant(f, g1, g2, err):
    x0 = g1
    x1 = g2
    root = x1
    while fabs(f(x1)) > err and f(x0) != f(x1):
         x2 = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
         x0 = x1
         x1 = x2
         root = x2
    return root
print("The root of sin(x) + cos(x): ", secant(lambda x: (sin(x) + cos(x)), pi/2, 3*pi/2, 1e-6))
print("The root of sin(x) + cos(x): ", secant(lambda x: sin(x)+cos(x), -pi/2, pi/2, 1e-6))
print("The root of sin(x) + cos(x): ", secant(lambda x: (x**3), 5, 6, 1e-9))