from src.descriptors import PositiveFloat
from src.figures.figure import Figure


class Rectangle(Figure):

    a = PositiveFloat()
    b = PositiveFloat()

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def perimeter(self):
        return (self.a + self.b) * 2

    @property
    def area(self):
        return self.a * self.b
