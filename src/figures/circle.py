from cmath import pi
from src.descriptors import NonNegative
from src.figures.figure import Figure


class Circle(Figure):

    radius = NonNegative()

    def __init__(self, r):
        self.radius = r

    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return self.radius ** 2 * pi

    @property
    def perimeter(self):
        return self.radius * 2 * pi
