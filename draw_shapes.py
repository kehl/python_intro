__author__ = 'lois'
import turtle
import geom_formulae

def draw_rectangle(l,b):#drawing a rectangle
    turtle.forward(l) #length of rectangle
    turtle.left(90) #angle of corner of rectangle
    turtle.forward(b)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(b)
    turtle.left(90)
    turtle.done()

if __name__ == "__main__":
    draw_rectangle(50, 30)
    draw_rectangle(300, 200)



def draw_triangle(b,h):#drawing a triangle.
    turtle.forward(b)
    turtle.left(120)
    turtle.forward(h)
    turtle.left(120)
    turtle.forward(h)
    turtle.left(120)
    turtle.done()

if __name__ == "__main__":
    draw_triangle(30, 30)
    draw_triangle(400, 400)


def draw_parallelogram(sideA,sideB):#drawing a parallelogram.
    turtle.forward(sideA)
    turtle.left(60)
    turtle.forward(sideB)
    turtle.left(120)
    turtle.forward(sideA)
    turtle.left(60)
    turtle.forward(sideB)
    turtle.left(120)
    turtle.done()

if __name__ == "__main__":
    draw_parallelogram(50, 30)
    draw_parallelogram(300, 200)


def draw_circle(pi,r):  # drawing a circle
    turtle.circle(150) #radus of circle
    turtle.done()

if __name__ == "__main__":
    draw_circle(3.143,75)
