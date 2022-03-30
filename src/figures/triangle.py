from math import sqrt
from src.figures.figure import Figure


class Triangle(Figure):

    @staticmethod
    def check_if_exists(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def __new__(cls, a, b, c):
        if Triangle.check_if_exists(a, b, c):
            return super().__new__(cls)
        return None

    def __init__(self, a, b, c):
        super().__init__(a, b, c)

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        if isinstance(value, tuple) and len(value) == 3 and Triangle.check_if_exists(*value):
            self._dimensions = value
        else:
            raise(ValueError('Wrong data'))

    @property
    def perimeter(self):
        return sum(self.dimensions)

    @property
    def area(self):
        return sqrt((self.perimeter / 2 - self.dimensions[0]) *
                    (self.perimeter / 2 - self.dimensions[1]) *
                    (self.perimeter / 2 - self.dimensions[2]) *
                    self.perimeter / 2)
