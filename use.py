from figures import triangle
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.square import Square
from figures.triangle import Triangle

circle = Circle(5)
print(circle.name)
print(circle.radius)
print(circle.perimeter)
print(circle.area)

square = Square(10)
print(square.name)
print(square.side)
print(square.perimeter)
print(square.area)

rectangle = Rectangle(5, 10)
print(rectangle.name)
print(rectangle.dimensions)
print(rectangle.perimeter)
print(rectangle.area)

triangle = Triangle(5, 10, 12)
print(triangle.name)
print(triangle.dimensions)
print(triangle.perimeter)
print(triangle.area)

print(circle.add_area(rectangle))
