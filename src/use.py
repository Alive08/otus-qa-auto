from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.square import Square
from figures.triangle import Triangle

circle = Circle(2)
print(circle.name)
print(circle.radius)
circle.radius = 10
print(circle.perimeter)
print(circle.area)

square = Square(10)
print(square.name)
print(square.side)
square.side = 5
print(square.perimeter)
print(square.area)

rectangle = Rectangle(5, 10)
print(rectangle.name)
# rectangle.dimensions = 1,2
print(rectangle.dimensions)
print(rectangle.perimeter)
print(rectangle.area)

triangle = Triangle(10,12,15)
print(triangle.name)
print(triangle.dimensions)
triangle.dimensions = 20,25,23
print(triangle.perimeter)
print(triangle.area)

foo = (2,33,4)

print(circle.add_area(triangle))
