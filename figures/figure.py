from queue import Empty
<<<<<<< HEAD

class Figure():

=======

class Figure():
>>>>>>> af83e24860f0761945e90660e04be88715313dc1
    def __init__(self, *arg):
        self.dimensions = arg
        self.name = 'A ' + type(self).__name__.lower()
    
    def _set_dimensions(self, value):
        if (value is None):
<<<<<<< HEAD
            raise(ValueError('No params defined'))
        if len(value) > 3:
            raise(ValueError('Too many params'))
        self._dimensions = value

    def _get_dimensions(self):
        return self._dimensions

    dimensions = property(
        fget=_get_dimensions,
        fset=_set_dimensions,
        fdel=None,
        doc="The Dimensions property"
    )

=======
            raise(ValueError('Empty value'))

        if len(value) > 3:
            raise(ValueError('Too many params'))
        else:
            self._dimensions = value

    def _get_dimensions(self):
        return self._dimensions

    dimensions = property(
        fget=_get_dimensions,
        fset=_set_dimensions,
        fdel=None,
        doc="The Dimensions property"
    )

>>>>>>> af83e24860f0761945e90660e04be88715313dc1
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
<<<<<<< HEAD
            raise(ValueError('The argument is not a Figure'))
=======
            raise(ValueError('The argument is not a Figure'))
>>>>>>> af83e24860f0761945e90660e04be88715313dc1
