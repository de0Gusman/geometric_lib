import pytest
from math import pi
from circle import area, perimeter


def test_area():
    radius = 2
    res = area(radius)
    assert res == 4 * pi


def test_perimeter():
    radius = 2
    res = perimeter(radius)
    assert res == 4 * pi


def test_area_zero():
    radius = 0
    res = area(radius)
    assert res == 0


def test_perimeter_zero():
    radius = 0
    res = perimeter(radius)
    assert res == 0


def test_area_neg():
    radius = -2
    with pytest.raises(AssertionError):
        area(radius)


def test_perimeter_neg():
    radius = -2
    with pytest.raises(AssertionError):
        perimeter(radius)
