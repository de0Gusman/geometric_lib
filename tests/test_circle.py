import pytest
from math import pi
from circle import area, perimeter


def test_area_of_circle():
    radius = 4
    result = area(radius)
    assert result == 16 * pi


def test_perimeter_of_circle():
    radius = 4
    result = perimeter(radius)
    assert result == 8 * pi


def test_area_with_zero_radius():
    radius = 0
    result = area(radius)
    assert result == 0


def test_perimeter_with_zero_radius():
    radius = 0
    result = perimeter(radius)
    assert result == 0


def test_area_with_negative_radius():
    radius = -4
    with pytest.raises(AssertionError):
        area(radius)


def test_perimeter_with_negative_radius():
    radius = -4
    with pytest.raises(AssertionError):
        perimeter(radius)
