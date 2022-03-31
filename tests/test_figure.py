import pytest
from src.figures.figure import Figure


@pytest.fixture
def subclass_instance():

    class F(Figure):
        pass

    return F()


def test_base_class_can_not_instantiate():
    assert Figure() is None


def test_subclass_can_instantiate(subclass_instance):
    assert subclass_instance is not None


def test_subclass_str(subclass_instance):
    assert str(subclass_instance) == 'f'


@pytest.mark.parametrize('param', [('area'), ('perimeter')])
def test_not_implemented_attrs(subclass_instance, param):
    with pytest.raises(NotImplementedError):
        getattr(subclass_instance, param)


def test_add_area_does_not_take_non_figure_instance(subclass_instance):
    with pytest.raises(TypeError):
        subclass_instance.add_area('Not a Figure but a String')


def test_add_area_takes_figure_instance(subclass_instance):
    with pytest.raises(NotImplementedError):
        subclass_instance.add_area(subclass_instance)
