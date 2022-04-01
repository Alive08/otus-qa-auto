import pytest
from src.figures.rectangle import Rectangle

test_data = [((None, None), False), ((-10, 10), False), ((10, 0), False),
             ((10, 20), True), ((11.11, 12.12), True), ((0.01, 0.42), True),
             ((1, 2), True), ([1, 2, 3], False), (('9', 5), False)]


@pytest.mark.parametrize("dimensions, expected", test_data)
def test_create_instance(dimensions, expected):
    r = None
    try:
        r = Rectangle(*dimensions)
    except Exception:
        pass
    else:
        assert (r.a, r.b) == dimensions
    assert isinstance(r, Rectangle) == expected


@pytest.mark.parametrize("dimensions, expected", test_data)
def test_set_side(dimensions, expected):
    s = Rectangle(1, 1)
    try:
        s.a, s.b = dimensions
    except Exception:
        assert not expected
    else:
        assert (s.a, s.b) == dimensions
        assert expected


def test_str():
    assert str(Rectangle(1, 1)) == 'rectangle'


def test_area():
    assert Rectangle(5, 10).area == 50


def test_perimeter():
    assert Rectangle(2.5, 1.4).perimeter == 7.8


def test_add_area():
    assert Rectangle(2.5, 1.4).add_area(Rectangle(2, 3)) == 9.5
