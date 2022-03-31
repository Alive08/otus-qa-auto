class PositiveFloat:
    "Дескриптор для работы с положительными ненулевыми вещественными числами"

    @classmethod
    def verify_number(cls, number):
        if type(number) not in (int, float) or number <= 0:
            raise TypeError("Параметр должен быть положительным числом больше нуля")

    def __set_name__(self, owner, name):
        self.name = "__" + name

    def __get__(self, obj, owner):
        return getattr(obj, self.name)

    def __set__(self, obj, value):
        self.verify_number(value)
        setattr(obj, self.name, value)

    def __delete__(self, obj):
        pass


class NotImplementedAttribute:
    "Дескриптор для нереализованных аттрибутов"

    def __get__(self, *args):
        raise NotImplementedError("Не реализовано")

    def __set__(self, *args):
        raise NotImplementedError("Не реализовано")
