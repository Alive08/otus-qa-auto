from .figure import Figure

class Rectangle(Figure):

    def __init__(self, *arg):
        super().__init__(*arg)
        if(len(self.dimensions) != 2):
            raise(ValueError('Wrong params number'))

    area = property(lambda self: self.dimensions[0] * self.dimensions[1])

    perimeter = property(lambda self: (self.dimensions[0] + self.dimensions[1]) * 2)
<<<<<<< HEAD
=======

>>>>>>> af83e24860f0761945e90660e04be88715313dc1
