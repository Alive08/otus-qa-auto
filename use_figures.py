from src.figures.circle import Circle
from src.figures.square import Square
from src.figures.rectangle import Rectangle
from src.figures.triangle import Triangle


# c = Circle(10)
# print(c.radius)
# c.radius = 15
# print(c.area)
# print(c.perimeter)
# print(c.__dict__)

s = Square(2)
print(s.__dict__)
s.a = 4
print(s.__dict__)
print(s.a)
s.a = 8
print(s.area)
print(s.perimeter)
print(str(s))


# r = Rectangle(3, 5)
# print(r.a, r.b)
# r.a, r.b = 6, 7
# print(r.a, r.b)
# print(r.area)
# print(r.perimeter)
# print(r.__dict__)

# t = Triangle(10, 12, 15)
# print(t.a, t.b, t.c)
# t.a, t.b, t.c = 12, 15, 19
# print(t.a, t.b, t.c)
# print(t.area)
# print(t.perimeter)
# print(t.__dict__)

# print(c.add_area(t))
