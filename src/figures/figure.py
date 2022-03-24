class Figure():

    def __init__(self, *args):

        self.name = 'A ' + type(self).__name__.lower()
        self._dimensions = args

    @property
    def _dimensions(self):
        return self._dimensions_data

    @_dimensions.setter
    def _dimensions(self, value):
        try:
            self._dimensions_data = tuple(float(v) for v in value)
        except ValueError as e:
            print(type(e), e)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def add_area(self, figure):
        if (isinstance(figure, Figure)):
            return self.area + figure.area
        else:
            raise(ValueError('The object given is not an instance of the Figure'))
