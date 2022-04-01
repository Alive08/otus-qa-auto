class Figure():
    "Базовый класс для геометрической фигуры"

    def __new__(cls, *args, **kw):
        "Запрет на создание экземпляров базового класса"
        return None if cls is Figure else super().__new__(cls)

    def __str__(self):
        return type(self).__name__.lower()

    def add_area(self, figure):
        if isinstance(figure, Figure):
            return self.area + figure.area
        else:
            raise TypeError(
                "The object given is not an instance of the Figure class")
