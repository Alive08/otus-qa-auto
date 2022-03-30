from cmath import pi
from src.figures.figure import Figure
from src.utils import validate_number

class Circle(Figure):

    def __init__(self, *args):
        if (len(args) != 1):
            raise(ValueError('Should be one number here'))
        super().__init__(*args)

    @property
    def radius(self):
        return self._dimensions[0]
    
    @radius.setter   
    def radius(self, value):
        if validate_number(value):
            self._dimensions = value,
    
    @property
    def diameter(self):
        return self.radius * 2

    @property
    def area(self):
        return self.radius ** 2 * pi

    @property
    def perimeter(self):
        return self.radius * 2 * pi
