from .figure import Figure

class Square(Figure):

    def __init__(self, *arg):
        super().__init__(*arg)
        if(len(self.dimensions) != 1):
            raise(ValueError('Wrong params number'))

    def _get_side(self):
        return self.dimensions[0]
    
    def _set_side(self, value):
        self.dimensions[0] = value
    
    side = property(
        fget=_get_side,
        fset=_set_side
    )

    area = property(lambda self: self.side ** 2)

    perimeter = property(lambda self: self.side * 4)
