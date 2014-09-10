__author__ = 'lois'

from numbers import Number
from math import *
from geom_formulae import*

def geom_validate(val):
    """
    Test if val is a Number and is >= 0.

    >>> geom_validate(5)
    True

    >>> geom_validate(-5)
    False

    >>> geom_validate("a string")
    False
    """
    return isinstance(val, Number) and val >= 0

print(geom_validate(5))

def triangle_area(base, height):
    """

    :param base: length of base
    :param height:height of triangle
    :return:
    >>> triangle_area(6, 5)
    15.0
    """
    if (geom_validate(base)) and (geom_validate(height)) :
        return 0.5*base*height
    else:
        raise ValueError("base or height is less than 0: "+str(base,height))
    #user gets informed about the wrong entry

def triangle_perimeter(side1,side2, side3):
    """

    :param side1:left side of triangle
    :param side2:right side of triangle
    :param side3:base side of triangle
    :return:
    >>> triangle_perimeter(6,6,4)
    16
    """
    if (geom_validate(side1)) and (geom_validate(side2)) and (geom_validate(side3)):
        return side1+ side2+side3
    else:
        raise ValueError("base or height is less than 0: "+str(side1,side2,side3))


if __name__ == "__main__":
    print("area:",triangle_area(6,5))
    print("perimeter:", triangle_perimeter(6,6,4))


def rectangle_area(length, width):
    """
    :param length: length of rectangle
    :param width: width of rectangle
    :return:
    >>> rectangle_area(3,7)
    21
    """
    if (geom_validate(length)) and (geom_validate(width)) :
       return length*width
    else:
        raise ValueError("base or height is less than 0: "+str(length,width))




def rectangle_perimeter(length, width):

    if (geom_validate(length)) and (geom_validate(width)) :
       return 2*(length + width)
    else:
        raise ValueError("base or height is less than 0: "+str(length,width))


if __name__ == "__main__":
    print("rec_area:",rectangle_area(3,7))
    print ("rec_perimeter:", rectangle_perimeter(3,7))


