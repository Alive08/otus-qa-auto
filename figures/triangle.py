from math import sqrt
from .figure import Figure

class Triangle(Figure):
<<<<<<< HEAD
    
=======
>>>>>>> af83e24860f0761945e90660e04be88715313dc1
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
