__author__ = 'lois'
from Objects import *
shape_dict = {'1': 'Rectangle', '2': 'Parallelogram', '3': 'Equilateral_Triangle', '4': 'Circle'}

print('Welcome!!! Choose a shape and let us try to compute its properties.'
      ' Please type each word as you see below'
      ':\n Rectangle, Parallelogram, Equilateral_Triangle, Circle')
print('or  QUIT.')
#first prompt of the mode


def start():
    figure = input("Enter the name of your shape , 'quit' to stop:")
    while figure != "quit":
        if figure != "quit" and figure in shape_dict.get('1'):               #rectangle
            try:
                length = float(input("Enter length measurement, 'quit' to stop:"))
                breadth = float(input("Enter breadth measurement, 'quit' to stop:"))
                rec = Rectangle(length, breadth)
                print(rec)
                rec.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()
        elif figure != "quit" and figure in shape_dict.get('2'):               #parallelogram
            try:
                base = float(input("Enter base measurement, 'quit' to stop:"))
                height = float(input("Enter perpendicular height measurement, 'quit' to stop:"))
                slant_height = float(input("Enter slant height measurement, 'quit' to stop:"))
                pal = Parallelogram(base, height, slant_height)
                print(pal)
                pal.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure != "quit" and figure in shape_dict.get('3'):         # equilateral_triangle)
            try:
                side = float(input("What is the side length? 'quit' to stop:"))
                tri = Equilateral_Triangle(side)
                print(tri)
                tri.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()

        elif figure != "quit" and figure in shape_dict.get('4'):         # circle
            try:
                radius = float(input("Enter your preferred radius, 'quit' to stop:"))
                circle = Circle(radius)
                print(circle)
                circle.draw()
            except ValueError as err:
                print(err.args[0])
            finally:
                return start()


        else:
            print('OOoopss!!!,Please check and input the right name of the shape.Begin each with upper case letter ')
            return start()
start()