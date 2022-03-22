from math import sqrt
from .figure import Figure

class Triangle(Figure):

    def __init__(self, *args):
        if (len(args) != 3):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    def _get_dimensions(self):
        return self._dimensions
    
    def _set_dimensions(self, value):
        if (isinstance(value, tuple) and len(value) == 3):
            self._dimensions = value
        else:
            raise(ValueError('Wrong args number'))
        
    dimensions = property(
        fget=_get_dimensions,
        fset=_set_dimensions
    )
    
    perimeter = property(lambda self: self.dimensions[0] + self.dimensions[1] + self.dimensions[2])

    _semi_perimeter = property(lambda self: self.perimeter / 2)

    area = property(lambda self: sqrt((self._semi_perimeter - self.dimensions[0]) *
                                      (self._semi_perimeter - self.dimensions[1]) *
                                      (self._semi_perimeter - self.dimensions[2]) *
                                       self._semi_perimeter))
