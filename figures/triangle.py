from math import sqrt
from .figure import Figure

class Triangle(Figure):
    
    def __init__(self, *arg):
        super().__init__(*arg)
        if(len(self.dimensions) != 3):
            raise(ValueError('Wrong params number'))
    
    perimeter = property(lambda self: self.dimensions[0] + self.dimensions[1] + self.dimensions[2])

    _semi_perimeter = property(lambda self: self.perimeter / 2)

    area = property(lambda self: sqrt((self._semi_perimeter - self.dimensions[0]) *
                                      (self._semi_perimeter - self.dimensions[1]) *
                                      (self._semi_perimeter - self.dimensions[2]) *
                                       self._semi_perimeter))
