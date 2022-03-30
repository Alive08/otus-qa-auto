from src.utils import validate_number


class Figure():
    "Обобщенный класс геометрической фигуры"

    def __new__(cls, *args, **kw):
        "Запрет на создание экземпляров базового класса"
        return None if cls is Figure else super().__new__(cls)

    def __init__(self, *args):
        self._dimensions = args

    def __str__(self):
        return type(self).__name__.lower()

    @property
    def _dimensions(self):
        return self.__dimensions_data

    @_dimensions.setter
    def _dimensions(self, value):
        if not value:
            raise ValueError('No data given')
        for v in value:
            validate_number(v)
        # кортеж, в котором хранятся данные о размерах фигуры
        self.__dimensions_data = value

    @property
    def area(self):
        raise NotImplementedError(
            f"Not implemented in the {type(self).__name__} class")

    @area.setter
    def area(self, *args):
        raise NotImplementedError(
            f"Not implemented in the {type(self).__name__} class")

    @property
    def perimeter(self):
        raise NotImplementedError(
            f"Not implemented in the {type(self).__name__} class")

    @perimeter.setter
    def area(self, *args):
        raise NotImplementedError(
            f"Not implemented in the {type(self).__name__} class")

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError(
                "The object given is not an instance of the Figure class")
