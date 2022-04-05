import pytest
from src.figures.circle import Circle
from src.figures.figure import Figure
from src.figures.rectangle import Rectangle
from src.figures.square import Square
from src.figures.triangle import Triangle


@pytest.fixture
def subclass_instance():
    class F(Figure):
        pass
    return F()


@pytest.fixture
def circle_valid():
    return Circle(5)


@pytest.fixture
def rectangle_valid():
    return Rectangle(5, 10)


@pytest.fixture
def square_valid():
    return Square(5)


@pytest.fixture
def triangle_valid():
    return Triangle(12, 13, 15)


@pytest.fixture
def triangle_invalid():
    return (12, 13, 42)
