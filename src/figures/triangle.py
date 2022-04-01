from math import sqrt
from src.descriptors import NonNegative
from src.figures.figure import Figure


class Triangle(Figure):

    a = NonNegative()
    b = NonNegative()
    c = NonNegative()

    @staticmethod
    def check_if_exists(a, b, c):
        return a > 0 and b > 0 and c > 0 and \
            a + b > c and a + c > b and b + c > a

    def __new__(cls, a, b, c):
        if Triangle.check_if_exists(a, b, c):
            return super().__new__(cls)

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def __setattr__(self, __name, __value):
        # проверять только при изменении размеров
        if __name in ('a', 'b', 'c'):
            # если объект уже был полностью иницииализирован ранее
            d = self.__dict__.copy()
            if all(('__a' in d, '__b' in d, '__c' in d)):
                d[f"__{__name}"] = __value
                if not self.check_if_exists(d['__a'], d['__b'], d['__c']):
                    raise(ValueError('Такой треугольник не существует'))

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
