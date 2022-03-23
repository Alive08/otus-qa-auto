from .figure import Figure

class Square(Figure):

    def __init__(self, *args):
        if (len(args) != 1):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    @property
    def side(self):
        return self._dimensions[0]
    
    @side.setter
    def side(self, value):
        self._dimensions = value,

    @property
    def perimeter(self):
        return self.side * 4

    @property
    def area(self):
        return self.side ** 2
