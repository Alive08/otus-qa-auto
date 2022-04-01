import pytest
from src.figures.square import Square

test_data = [(None, False), (-10, False), (0, False),
             (10, True), (11.11, True), (0.01, True),
             ((1, 2), False), ([1, 2], False), ('9', False)]


@pytest.mark.parametrize("side, expected", test_data)
def test_create_instance(side, expected):
    s = None
    try:
        s = Square(side)
    except Exception:
        pass
    else:
        assert s.a == side
    assert isinstance(s, Square) == expected


@pytest.mark.parametrize("side, expected", test_data)
def test_set_side(side, expected):
    s = Square(1)
    try:
        s.a = side
    except Exception:
        assert not expected
    else:
        assert s.a == side
        assert expected


def test_str():
    assert str(Square(1)) == 'square'


def test_area():
    assert Square(5).area == 25


def test_perimeter():
    assert Square(5).perimeter == 20


def test_add_area():
    assert Square(2).add_area(Square(3)) == 13
