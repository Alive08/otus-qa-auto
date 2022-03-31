from src.descriptors import PositiveFloat
# from src.figures_descriptor.figure import Figure
from src.figures_descriptor.rectangle import Rectangle


class Square(Rectangle):

    a = PositiveFloat()
    b = a

    def __init__(self, a):
        self.a = a
