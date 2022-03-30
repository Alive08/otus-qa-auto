from src.figures.figure import Figure
from src.figures.circle import Circle
from src.figures.rectangle import Rectangle
from src.figures.square import Square
from src.figures.triangle import Triangle

circle = Circle(5)
circle.radius = 6

square = Square(10)
square.side = 8

rectangle = Rectangle(5, 10)
triangle = Triangle(10, 12, 15)

for f in (circle, square, rectangle, triangle):
    print(f"A {f} has dimensions {f._dimensions}, perimeter of {f.perimeter:.2f} and area of {f.area:.2f}")

try:
    triangle.dimensions = 10, 12, 19
except ValueError:
    print('Wrong dimensions')

print(circle.add_area(triangle))
