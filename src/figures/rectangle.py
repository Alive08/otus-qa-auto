from .figure import Figure

class Rectangle(Figure):

    def __init__(self, *args):
        if (len(args) != 2):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    def _get_dimensions(self):
        return self._dimensions
    
    def _set_dimensions(self, value):
        if isinstance(value, tuple) and len(value) == 2 :
            self._dimensions = value
        else:
            raise(ValueError('Wrong args number'))
        
    dimensions = property(
        fget=_get_dimensions,
        fset=_set_dimensions
    )

    area = property(lambda self: self.dimensions[0] * self.dimensions[1])

    perimeter = property(lambda self: (self.dimensions[0] + self.dimensions[1]) * 2)
