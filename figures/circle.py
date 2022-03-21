from cmath import pi
from posixpath import dirname
from .figure import Figure

class Circle(Figure):

    def __init__(self, dimension):
        self.set_name('A circle')
        self.radius = dimension
    
    def _set_radius(self, value):
        self._radius = value

    def _get_radius(self):
        return self._radius

    radius = property(
        fget=_get_radius,
        fset=_set_radius,
        fdel=None,
        doc="The radius property"
    )

    area = property(lambda self: self._radius ** 2 * 4 * pi)

    perimeter = property(lambda self: self._radius * 2 * pi)

    def add_area(self, figure):
        pass
