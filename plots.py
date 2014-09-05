__author__ = 'lois'
from pylab import *

from geom_formulae import *

# make functions able to operate on vectors
v_rectyangle_area = np.vectorize(rectangle_area)
v_rectangle_perimeter = np.vectorize(rectangle_perimeter)

def square_plot_props(start, end):
    """
    Plot the area and perimeter of a square as a function of side
    length, with side length from start to end.
    @param start: starting value.  should be less than end.
    @param end: end value.  should be greater than start.
    @return: None.  Produces a plot.
    """
    S = np.linspace(start, end) # our side lengths
    A = v_rectangle_area(S)  # the areas
    P = v_rectangle_perimeter(S)  # the perimeters
    plot(S, A, '-r', label="Area")
    plot(S, P, ':b', label="Perimeter")
    xlabel('side length')
    ylabel('geo values')
    title('Square Geo Properties')
    legend(loc='upper right')
    show()
    pass

if __name__ == "__main__":
    rectangle_plot_props(0, 5)