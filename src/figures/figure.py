class Figure():
    "Базовый класс для геометрической фигуры"

    def __new__(cls, *args, **kwargs):
        if cls is Figure:
            raise ValueError("Невозможно создать объект этого класса")
        return super().__new__(cls)

    def __init__(self):
        self.name = self.__str__()

    def __str__(self):
        return type(self).__name__.lower()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise ValueError("Переданный объект не является фигурой")
