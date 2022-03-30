import pytest
from src.figures.figure import Figure

test_data =[
    ((1), 0),
    ((1,), 1),
    ((1,2,3), 3),
    (('1.0','2.0','3.0'), 3),
    (('l',2,'З'), 0) ]

class TestFigure():

    f = Figure()

    def test_name(self):
        assert self.f.name == 'A figure'

    @pytest.mark.parametrize('param, expected', test_data)
    def test_set_dimensions(self, param, expected):
        self.f._dimensions = ()
        try:
            self.f._dimensions = param
        except:
            pass
        assert len(self.f._dimensions) == expected
    
    def test_get_dimensions(self):
        data = (1, '2', 3.333)
        self.f._dimensions = data
        assert self.f._dimensions == (1, 2.0, 3.333)
