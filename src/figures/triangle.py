from math import sqrt
from src.descriptors import NonNegative
from src.figures.figure import Figure


class Triangle(Figure):

    a = NonNegative()
    b = NonNegative()
    c = NonNegative()
    __initialized = False

    @staticmethod
    def check_if_exists(a, b, c):
        return all((a + b > c, a + c > b, b + c > a))

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if not Triangle.check_if_exists(a, b, c):
            raise ValueError(f'Треугольник {a, b, c} не существует')
        super().__init__()
        self.__initialized = True

    def __setattr__(self, __name, __value):
        '''
        ограничение реализации - проверяем при изменении размеров
        только если объект уже был полностью иницииализирован ранее
        '''
        print("__setattr__: ", __name, __value)
        if __name in ('a', 'b', 'c'):
            NonNegative.verify_number(__value)
            if self.__initialized:
                d = self.__dict__.copy()
                d[f"__{__name}"] = __value
                if not Triangle.check_if_exists(d['__a'], d['__b'], d['__c']):
                    raise(ValueError(
                        f'Треугольник {tuple(d.values())} не существует'))
        return super().__setattr__(__name, __value)

    @property
    def perimeter(self):
        return self.a + self.b + self.c

    @property
    def area(self):
        return sqrt((self.perimeter / 2 - self.a) *
                    (self.perimeter / 2 - self.b) *
                    (self.perimeter / 2 - self.c) *
                    self.perimeter / 2)
