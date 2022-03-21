from cmath import pi
from .figure import Figure

class Circle(Figure):

    def __init__(self, *arg):
        super().__init__(*arg)
        if(len(self.dimensions) != 1):
            raise(ValueError('Wrong params number'))

    def _get_radius(self):
        return self.dimensions[0]
    
    def _set_radius(self, value):
        self.dimensions[0] = value
    
    radius = property(
        fget=_get_radius,
        fset=_set_radius
    )

    area = property(lambda self: self.radius ** 2 * 4 * pi)

    perimeter = property(lambda self: self.radius * 2 * pi)

