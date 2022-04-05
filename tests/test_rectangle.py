import pytest
from src.figures.rectangle import Rectangle

test_data = [((None, None), False),
             ((None, 10), False),
             ((-10, 10), False),
             ((10, 0), False),
             (('9', 5), False),
             ([1, 2, 3], False),
             ((1, 2, 3), False),
             ((11.11, 12.12), True),
             ((0.01, 0.42), True),
             ((5, 10), True),
             ((5.5, 10), True)]


@ pytest.mark.parametrize("dimensions, expected", test_data)
def test_create_instance(dimensions, expected):
    try:
        r = Rectangle(*dimensions)
    except (ValueError, TypeError):
        assert not expected
    else:
        assert (r.a, r.b) == dimensions
        assert isinstance(r, Rectangle) == expected


@ pytest.mark.parametrize("dimensions, expected", test_data)
def test_set_side(dimensions, expected, rectangle_valid):
    try:
        rectangle_valid.a, rectangle_valid.b = dimensions
    except ValueError:
        assert not expected
    else:
        assert (rectangle_valid.a, rectangle_valid.b) == dimensions


def test_str(rectangle_valid):
    assert str(rectangle_valid) == 'rectangle'


def test_area(rectangle_valid):
    assert rectangle_valid.area == 50


def test_perimeter(rectangle_valid):
    assert rectangle_valid.perimeter == 30
