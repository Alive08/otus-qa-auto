import pytest
from src.figures.square import Square

test_data = [(None, False),
             (-10, False),
             (0, False),
             ('9', False),
             ((1,), False),
             ([1, 10], False),
             ({'radius': 1}, False),
             (0.01, True),
             (10, True),
             (42.42, True)]


@pytest.mark.parametrize("side, expected", test_data)
def test_create_instance(side, expected):
    try:
        s = Square(side)
    except ValueError:
        assert not expected
    else:
        assert s.a == side
        assert isinstance(s, Square) == expected


@pytest.mark.parametrize("side, expected", test_data)
def test_set_side(side, expected, square_valid):
    try:
        square_valid.a = side
    except ValueError:
        assert not expected
    else:
        assert square_valid.a == side


def test_str(square_valid):
    assert str(square_valid) == 'square'


def test_area(square_valid):
    assert square_valid.area == 25


def test_perimeter(square_valid):
    assert square_valid.perimeter == 20
