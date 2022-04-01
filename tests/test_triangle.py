import pytest
from src.figures.triangle import Triangle

test_data = [((None, None, None), False),
             (('12', '13', '15'), False),
             ((-12, 13, 15), False),
             ((0, 12, 13), False),
             ((12, 13, 30), False),
             ((12, 13, 15), True)]


@pytest.fixture
def triangle_valid():
    return (12, 13, 15)


@pytest.fixture
def triangle_invalid():
    return (12, 13, 42)


def test_can_create_valid_instance(triangle_valid):
    assert isinstance(Triangle(*triangle_valid), Triangle)


def test_can_not_create_invalid_instance(triangle_invalid):
    assert Triangle(*triangle_invalid) is None


@pytest.mark.parametrize("dimensions, expected", test_data)
def test_create_instance(dimensions, expected):
    t = None
    try:
        t = Triangle(*dimensions)
    except Exception:
        pass
    assert isinstance(t, Triangle) == expected
    if t is not None:
        assert (t.a, t.b, t.c) == dimensions


@pytest.mark.parametrize("dimensions, expected", test_data)
def test_set_dimensions(dimensions, expected, triangle_valid):
    t = Triangle(*triangle_valid)
    try:
        t.a, t.b, t.c = dimensions
    except Exception:
        assert not expected
    else:
        assert (t.a, t.b, t.c) == dimensions
        assert expected


def test_str(triangle_valid):
    assert str(Triangle(*triangle_valid)) == 'triangle'


def test_area(triangle_valid):
    assert round(Triangle(*triangle_valid).area, 2) == 74.83


def test_perimeter(triangle_valid):
    assert Triangle(*triangle_valid).perimeter == 40


def test_add_area(triangle_valid):
    assert round(Triangle(*triangle_valid).add_area(
        Triangle(*triangle_valid)), 2) == 149.67
