from src.descriptors import NonNegative
from src.figures.rectangle import Rectangle


class Square(Rectangle):

    b = a = NonNegative()

    def __init__(self, a):
        self.a = a
