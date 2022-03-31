from src.figures_property.figure import Figure


class Rectangle(Figure):

    def __init__(self, a, b):
        super().__init__(a, b)

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, value):
        if isinstance(value, tuple) and len(value) == 2:
            self._dimensions = value
        else:
            raise(ValueError('Wrong data'))

    @property
    def perimeter(self):
        return sum(self.dimensions) * 2

    @property
    def area(self):
        return self.dimensions[0] * self.dimensions[1]
