import pytest
from triangle import area, perimeter


def test_area():
    x, y, z = 5, 12, 13
    res = area(x, y, z)
    assert res == 30


def test_area_zero():
    x, y, z = 0, 0, 0
    res = area(x, y, z)
    assert res == 0


def test_perimeter():
    x, y, z = 5, 12, 13
    res = perimeter(x, y, z)
    assert res == 30


def test_perimeter_zero():
    x, y, z = 0, 0, 0
    res = perimeter(x, y, z)
    assert res == 0


def test_area_neg():
    x, y, z = -5, -12, -13
    with pytest.raises(AssertionError):
        area(x, y, z)


def test_perimeter_neg():
    x, y, z = -5, -12, -13
    with pytest.raises(AssertionError):
        perimeter(x, y, z)
