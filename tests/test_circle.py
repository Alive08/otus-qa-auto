from math import pi

import pytest
from src.figures.circle import Circle

test_data = [(None, False),
             (-10, False),
             (0, False),
             ('9', False),
             ((1,), False),
             ([1, 2], False),
             ({'radius': 1}, False),
             (0.01, True),
             (10, True),
             (42.42, True)]


@pytest.mark.parametrize("radius, expected", test_data)
def test_create_instance(radius, expected):
    try:
        c = Circle(radius)
    except ValueError:
        assert not expected
    else:
        assert c.radius == radius
        assert isinstance(c, Circle) == expected


@pytest.mark.parametrize("radius, expected", test_data)
def test_set_radius(radius, expected, circle_valid):
    try:
        circle_valid.radius = radius
    except ValueError:
        assert not expected
    else:
        assert circle_valid.radius == radius


def test_str(circle_valid):
    assert str(circle_valid) == 'circle'


def test_diameter(circle_valid):
    assert circle_valid.diameter == 10


def test_area(circle_valid):
    assert circle_valid.area == pi * 25


def test_perimeter(circle_valid):
    assert circle_valid.perimeter == pi * 10
