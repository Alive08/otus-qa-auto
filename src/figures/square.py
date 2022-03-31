from src.descriptors import PositiveFloat
from src.figures.rectangle import Rectangle


class Square(Rectangle):

    a = b = PositiveFloat()

    def __init__(self, a):
        self.a = a
