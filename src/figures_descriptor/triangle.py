from math import sqrt
from src.descriptors import PositiveFloat
from src.figures_descriptor.figure import Figure


class Triangle(Figure):

    a = PositiveFloat()
    b = PositiveFloat()
    c = PositiveFloat()

    @staticmethod
    def check_if_exists(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __new__(cls, a, b, c):
        if Triangle.check_if_exists(a, b, c):
            return super().__new__(cls)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return sqrt((self.perimeter / 2 - self.a) *
                    (self.perimeter / 2 - self.b) *
                    (self.perimeter / 2 - self.c) *
                    self.perimeter / 2)
