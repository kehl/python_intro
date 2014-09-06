__author__ = 'lois'

from numbers import Number
from math import *

def triangle_area(base, height):
    """

    :param base: length of base
    :param height:height of triangle
    :return:
    >>> triangle_area(6, 5)
    15
    """
    return 0.5*base*height


def triangle_perimeter(side1,side2, side3):
    """

    :param side1:left side of triangle
    :param side2:right side of triangle
    :param side3:base side of triangle
    :return:
    >>>triangle_perimeter(6,6,4)
    16
    """
    return side1+ side2+side3

if __name__ == "__main__":
    print("area:",triangle_area(6,5))
    print("perimeter:", triangle_perimeter(6,6,4))


def rectangle_area(length, width):
    """
    :param length: length of rectangle
    :param width: width of rectangle
    :return:
    >>>rectangle_area(3,7)
    21
    """
    return length*width


def rectangle_perimeter(length, width):
    return 2*(length + width)


if __name__ == "__main__":
    print("rec_area:",rectangle_area(3,7))
    print ("rec_perimeter:", rectangle_perimeter(3,7))



def parallelogram_area(base,height):
    """

    :param base: base of parallelogram
    :param height: height of parallelogram
    :return:
    >>>parallelogram_area (5, 7)
    35
    """
    return base * height


def parallelogram_perimeter(sideA,sideB):
    """

    :param sideA: right and left sides of paralelogram
    :param sideB:top and bottom of parallelogram
    :return:
    >>>parallelogram_perimeter(6,5)
    22
    """
    return 2*(sideA+sideB)

if __name__ == "__main__":
    print ("par_area:", parallelogram_area(5,7))
    print ("par_perimeter",parallelogram_perimeter(6,5))


def circle_area(radius):
    """
    this computes the area of a circle with a radius.
    :param radius:half the diameter of a circle
    :return:
    >>> circle_area (6)
    113.148
    """
    return pi*radius*radius

if __name__ == "__main__":
    print("cir_area",circle_area(6))

def circle_circumference(radius):
    """
    this computes the circumference of a circle.
    :param radius: half the diameter of a circle
    :return:
    >>> circle_circumference(6)
    37.715
    """
    return 2*pi*radius

if __name__ == "__main__":
    print("cir_circumference:",circle_circumference(6))
