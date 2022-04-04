from src.figures.figure import Figure
from src.figures.circle import Circle
from src.figures.square import Square
from src.figures.rectangle import Rectangle
from src.figures.triangle import Triangle


for figure in (Triangle(12, 13, 15), Circle(10), Rectangle(5, 10), Square(7)):
    print(
        f'A {figure} has perimeter {figure.perimeter:.2f} and area {figure.area:.2f}')
