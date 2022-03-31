from math import pi

import pytest
from src.figures.circle import Circle

test_data = [(None, False), (-10, False), (0, False),
             (10, True), (11.11, True), (0.01, True),
             ((1, 2), False), ([1, 2], False), ('9', False)]


@pytest.mark.parametrize("radius, expected", test_data)
def test_create_instance(radius, expected):
    c = None
    try:
        c = Circle(radius)
    except Exception:
        pass
    else:
        assert c.radius == radius
    assert isinstance(c, Circle) == expected
    


def test_str():
    assert str(Circle(1)) == 'circle'


@pytest.mark.parametrize("radius, expected", test_data)
def test_set_radius(radius, expected):
    c = Circle(1)
    try:
        c.radius = radius
    except Exception:
        assert not expected
    else:
        assert expected
        assert c.radius == radius


def test_diameter():
    assert Circle(5).diameter == 10


def test_area():
    assert Circle(2).area == pi * 4


def test_perimeter():
    assert Circle(2).perimeter == pi * 4


def test_add_area():
    assert Circle(2).add_area(Circle(1)) == pi * 5
