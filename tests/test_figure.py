from copy import copy

import pytest
from src.figures.figure import Figure


def test_base_class_can_not_instantiate():
    with pytest.raises(ValueError):
        Figure()


def test_subclass_can_instantiate(subclass_instance):
    assert isinstance(subclass_instance, Figure)


def test_subclass_str(subclass_instance):
    assert str(subclass_instance) == 'f'


def test_get_default_name():
    class FigureSubclass(Figure):
        pass
    assert FigureSubclass().name == 'figuresubclass'


def test_name():
    class FigureSubclass(Figure):
        pass
    name = "A Test Figure"
    f = FigureSubclass()
    f.name = name
    assert f.name == name


def test_add_area_does_not_take_non_figure_instance(subclass_instance):
    class C:
        area = 10
    with pytest.raises(ValueError):
        subclass_instance.add_area(C().area)


def test_add_area_takes_figure_instance(subclass_instance):
    subclass_instance.area = 5
    another_subclass_instance = copy(subclass_instance)
    another_subclass_instance.area = 15
    assert subclass_instance.add_area(another_subclass_instance) == 20
