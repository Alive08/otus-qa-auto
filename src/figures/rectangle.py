from src.descriptors import NonNegative
from src.figures.figure import Figure


class Rectangle(Figure):

    a = NonNegative()
    b = NonNegative()

    def __init__(self, a, b):
        self.a = a
        self.b = b
        super().__init__()

    @property
    def perimeter(self):
        return (self.a + self.b) * 2

    @property
    def area(self):
        return self.a * self.b
