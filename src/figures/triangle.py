from math import sqrt
from .figure import Figure

class Triangle(Figure):

    def __init__(self, *args):
        if (len(args) != 3):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    @property
    def dimensions(self):
        return self._dimensions
    
    @dimensions.setter
    def dimensions(self, value):
        if (isinstance(value, tuple) and len(value) == 3):
            self._dimensions = value
        else:
            raise(ValueError('Wrong args number'))
        
    @property    
    def perimeter(self):
        return sum(self.dimensions)

    @property
    def area(self):
        return sqrt((self.perimeter / 2 - self.dimensions[0]) *
                    (self.perimeter / 2 - self.dimensions[1]) *
                    (self.perimeter / 2 - self.dimensions[2]) *
                     self.perimeter / 2)
