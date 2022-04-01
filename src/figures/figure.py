from unicodedata import name


class Figure():
    "Базовый класс для геометрической фигуры"

    __not_implemented = (
        'perimeter',
        'area',
        'dimensions',
        'radius'
        'a',
        'b',
        'c'
    )

    def __new__(cls, *args, **kw):
        "Запрет на создание экземпляров базового класса"
        return None if cls is Figure else super().__new__(cls)

    def __getattr__(self, __name):
        if __name in self.__not_implemented:
            raise(NotImplementedError("Не реализовано в этом классе"))
        return super().__getattribute__(__name)

    def __setattr__(self, __name, __value):
        if __name in self.__not_implemented:
            raise(NotImplementedError("Не реализовано в этом классе"))
        super().__setattr__(__name, __value)

    def __str__(self):
        return type(self).__name__.lower()

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise TypeError(
                "The object given is not an instance of the Figure class")
