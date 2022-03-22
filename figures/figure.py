class Figure():

    def __init__(self, *args):

        self.name = 'A ' + type(self).__name__.lower()
        self._dimensions = args
        
    def _set_dimensions_data(self, value):
        for v in value:
            if not isinstance(v, (int, float)):
                raise(ValueError("Wrong args"))
        self._dimensions_data = value

    def _get_dimensions_data(self):
        return self._dimensions_data

    _dimensions = property(
        fget=_get_dimensions_data,
        fset=_set_dimensions_data
    )

    def _set_name(self, value):
        self._name = value
    
    def _get_name(self):
        return self._name

    name = property(
        fget=_get_name,
        fset=_set_name
    )
    
    def add_area(self, figure):
        if (isinstance(figure, Figure)):
            return self.area + figure.area
        else:
            raise(ValueError('The object given is not an instance of the Figure'))
