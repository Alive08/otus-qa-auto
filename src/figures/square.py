from src.figures.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, a):
        super().__init__(a, a)

    @property
    def side(self):
        return self._dimensions[0]

    @side.setter
    def side(self, value):
        self._dimensions = (value, value)
