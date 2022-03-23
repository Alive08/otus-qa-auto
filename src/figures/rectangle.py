from .figure import Figure

class Rectangle(Figure):

    def __init__(self, *args):
        if (len(args) != 2):
            raise(ValueError('Wrong args number'))
        super().__init__(*args)

    @property
    def dimensions(self):
        return self._dimensions
    
    @dimensions.setter
    def dimensions(self, value):
        if isinstance(value, tuple) and len(value) == 2 :
            self._dimensions = value
        else:
            raise(ValueError('Wrong args number'))

    @property
    def perimeter(self):
        return (self.dimensions[0] + self.dimensions[1]) * 2
    
    @property
    def area(self):
        return self.dimensions[0] * self.dimensions[1]
