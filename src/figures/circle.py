from cmath import pi
from .figure import Figure

class Circle(Figure):

    def __init__(self, *args):
        if (len(args) != 1):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    @property
    def radius(self):
        return self._dimensions[0]
    
    @radius.setter   
    def radius(self, value):
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
