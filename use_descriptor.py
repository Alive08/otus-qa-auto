from src.figures_descriptor.circle import Circle
from src.figures_descriptor.square import Square
from src.figures_descriptor.rectangle import Rectangle
from src.figures_descriptor.triangle import Triangle


c = Circle(10)
print(c.radius)
c.radius = 15
print(c.area)
print(c.perimeter)
print(c.__dict__)

s = Square(2)
print(s.a)
s.a = 5
print(s.area)
print(s.perimeter)
print(s.__dict__)


r = Rectangle(3, 5)
print(r.a, r.b)
r.a, r.b = 6, 7
print(r.a, r.b)
print(r.area)
print(r.perimeter)
print(r.__dict__)

t = Triangle(10, 12, 15)
print(t.a, t.b, t.c)
t.a, t.b, t.c = 12, 15, 19
print(t.a, t.b, t.c)
print(t.area)
print(t.perimeter)
print(t.__dict__)
