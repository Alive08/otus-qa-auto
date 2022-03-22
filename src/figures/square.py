from .figure import Figure

class Square(Figure):

    def __init__(self, *args):
        if (len(args) != 1):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    def _get_side(self):
        return self._dimensions[0]
    
    def _set_side(self, value):
        self._dimensions = value,
    
    side = property(
        fget=_get_side,
        fset=_set_side
    )

    area = property(lambda self: self.side ** 2)

    perimeter = property(lambda self: self.side * 4)
