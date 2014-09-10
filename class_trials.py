__author__ = 'lois'
from geom_formulae import *
from nose.tools import *


def rectangle_area_int():
    assert rectangle_area(1,2) == 2
    assert rectangle_area(2,5) == 10
    s = 5
    assert rectangle_area(s*2,2) == 2*rectangle_area(s,2)


def rectangle_area2():
    assert triangle_area(8,2) == 6
    assert triangle_area(2,5) == 10


@raises(TypeError)
def test_square_area_other():
    rectangle_area("a string")

def test_square_perimeter_int():
    s = 5
    assert rectangle_perimeter(s,2) == 20
    assert rectangle_perimeter(4*s,3) == rectangle_perimeter(s,3)*4