<<<<<<< HEAD
from figures.circle import Circle
from figures.rectangle import Rectangle
from figures.square import Square
from figures.triangle import Triangle
=======
from src.figures.circle import Circle
from src.figures.rectangle import Rectangle
from src.figures.square import Square
from src.figures.triangle import Triangle
>>>>>>> eda944938f91c7195e2c3cde5e7f0403653f7f30

circle = Circle(20)
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
<<<<<<< HEAD
# rectangle.dimensions = 1,2
=======
rectangle.dimensions = 1,2
>>>>>>> eda944938f91c7195e2c3cde5e7f0403653f7f30
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
