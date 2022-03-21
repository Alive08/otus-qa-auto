from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.square import Square
from figures.triangle import Triangle

circle = Circle(10)
print(circle.name)
print(circle.radius)
print(circle.perimeter)
print(circle.area)

circle.radius = 12

print(circle.radius)
print(circle.perimeter)
print(circle.area)


# rectangle = Rectangle()
# square = Square()
# triangle = Triangle()
