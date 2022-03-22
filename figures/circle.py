from cmath import pi
from .figure import Figure

class Circle(Figure):

    def __init__(self, *args):
        if (len(args) != 1):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    def _get_radius(self):
        return self._dimensions[0]
    
    def _set_radius(self, value):
        self._dimensions = value,
    
    radius = property(
        fget=_get_radius,
        fset=_set_radius
    )

    area = property(lambda self: self.radius ** 2 * 4 * pi)

    perimeter = property(lambda self: self.radius * 2 * pi)
