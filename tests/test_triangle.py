import pytest
from src.figures.triangle import Triangle

test_data = [((None, None, None), False),
             (('12', '13', '15'), False),
             ((-12, 13, 15), False),
             ((0, 12, 13), False),
             ((12, 13, 30), False),
             ((12, 13, 30, 35), False),
             ((12, 13, 15), True)]


def test_can_create_valid_instance(triangle_valid):
    assert isinstance(triangle_valid, Triangle)


def test_can_not_create_invalid_instance(triangle_invalid):
    with pytest.raises(ValueError):
        Triangle(*triangle_invalid)


@pytest.mark.parametrize("dimensions, expected", test_data)
def test_create_instance(dimensions, expected):
    try:
        t = Triangle(*dimensions)
    except (ValueError, TypeError):
        assert not expected
    else:
        assert (t.a, t.b, t.c) == dimensions
        assert isinstance(t, Triangle) == expected


@pytest.mark.parametrize("dimensions, expected", test_data)
def test_set_dimensions(dimensions, expected, triangle_valid):
    try:
        triangle_valid.a, triangle_valid.b, triangle_valid.c = dimensions
    except ValueError:
        assert not expected
    else:
        assert (triangle_valid.a, triangle_valid.b,
                triangle_valid.c) == dimensions


def test_str(triangle_valid):
    assert str(triangle_valid) == 'triangle'


def test_area(triangle_valid):
    assert round(triangle_valid.area, 2) == 74.83


def test_perimeter(triangle_valid):
    assert triangle_valid.perimeter == 40
