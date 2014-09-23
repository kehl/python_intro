__author__ = 'lois'
import turtle
from math import *
import math

def dim_checker(**kwargs):
    errmsg = "All given arguments must be positive numbers; provided :"\
             + \
             str({k: v for k, v in kwargs.items() if v is not None})
    for name, arg in kwargs.items():
        if arg is None:
            pass # ignore nones, only checking provided arguments here
        elif not isinstance(arg, (int, float)):
            raise TypeError(errmsg)
        elif not arg >= 0:
            raise ValueError(errmsg)


class Shape(object):
    shapes_created = 0
    def __init__(self, **kwargs):
        dim_checker(**kwargs)
        self.shapes_created += 1

    def __str__(self):
        return self.__class__.__name__ +\
            "; area : "+str(self.area)+\
            "; perimeter: "+str(self.perimeter)
class Equilateral_Triangle(Shape):
    """a class representation of an equilateral triangle"""
    equilateral_triangle_created = 0
    def __init__(self, side:(int,float)):
        super(Equilateral_Triangle, self).__init__(side=side)
        self.equilateral_triangle_created += 1
        self.side = side
        self.area = self.side**2 * math.sqrt(3)/4
        self.perimeter = 3*self.side

    def __str__(self):
        return super(Equilateral_Triangle, self).__str__()+"; side: "+str(self.side)

    def __cmp__(self, other):
        if not isinstance(other, Equilateral_Triangle):
            raise TypeError
        else:
            return self.side - other.side

    def draw(self):
       for _ in range(3):
           turtle.forward(self.side)
           turtle.left(120)
       Equilateral_Triangle(200)
       turtle.done()


if __name__ == "__main__":
    e_tri=Equilateral_Triangle(100)
    print(e_tri)
    e_tri.draw()


class Rectangle(Shape):
    """a class representation of a rectangle"""
    rectangle_created = 0
    def __init__(self, length:(int,float), breadth:(int,float)):
        super(Rectangle, self).__init__(length=length,breadth= breadth)
        self.rectangle_created += 1
        self.length = length
        self.breadth = breadth
        self.area = self.length * self.breadth
        self.perimeter = 2*(self.length + self.breadth)

    def __str__(self):
        return super(Rectangle, self).__str__()+"; length: "+str(self.length)+"; breadth: "+str(self.breadth)

    def __cmp__(self, other):
        if not isinstance(other, Rectangle):
            raise TypeError
        else:
            return self.length - other.length

    def draw(self):
        for i in range(2):
            turtle.forward(self.length)
            turtle.left(90)
            turtle.forward(self.breadth)
            turtle.left(90)
        Rectangle(100, 50)
        turtle.done()


if __name__ == "__main__":
    rec=Rectangle(100, 50)
    print(rec)
    rec.draw()

class Parallelogram(Shape):
    """a class representation of a parallelogram"""
    parallelogram_created = 0
    def __init__(self, base:(int,float), height:(int,float), slant_height: (int,float)):
        super(Parallelogram, self).__init__(base=base,height= height, slant_height = slant_height)
        self.parallelogram_created += 1
        self.base = base
        self.height = height
        self.slant_height = slant_height
        self.area = self.base * self.height
        self.perimeter = 2*(self.base + self.slant_height)

    def __str__(self):
        return super(Parallelogram, self).__str__()+"; base: "+str(self.base)+"; height: "+str(self.height)\
            + "; slant_height: "+str(self.slant_height)

    def __cmp__(self, other):
        if not isinstance(other, Parallelogram):
            raise TypeError
        else:
            return self.base - other.base

    def draw(self):
        for i in range(2):
           turtle.forward(self.base)
           turtle.left(60)
           turtle.forward(self.slant_height)
           turtle.left(120)
        Parallelogram(100, 50, 200)
        turtle.done()


if __name__ == "__main__":
    para=Parallelogram(100, 200, 50)
    print(para)
    para.draw()


class Circle(Shape):
    """a class representation of a circle"""
    circle_created = 0
    def __init__(self, radius:(int,float)):
        super(Circle, self).__init__(radius=radius)
        self.circle_created += 1
        self.radius = radius
        self.area = self.radius**2 * pi
        self.perimeter = 2 * pi * self.radius

    def __str__(self):
        return super(Circle, self).__str__()+"; radius: "+str(self.radius)

    def __cmp__(self, other):
        if not isinstance(other, Circle):
            raise TypeError
        else:
            return self.radius - other.radius

    def draw(self):
       turtle.circle(self.radius)
       Circle(150)
       turtle.done()


if __name__ == "__main__":
    circle=Circle(150)
    print(circle)
    circle.draw()
