import pytest
from triangle import area, perimeter


def test_triangle_area():
    a, b, c = 6, 8, 10
    result = area(a, b, c)
    assert result == 24


def test_area_with_zero_sides():
    a, b, c = 0, 0, 0
    result = area(a, b, c)
    assert result == 0


def test_triangle_perimeter():
    a, b, c = 6, 8, 10
    result = perimeter(a, b, c)
    assert result == 24


def test_perimeter_with_zero_sides():
    a, b, c = 0, 0, 0
    result = perimeter(a, b, c)
    assert result == 0


def test_area_with_negative_sides():
    a, b, c = -6, -8, -10
    with pytest.raises(AssertionError):
        area(a, b, c)


def test_perimeter_with_negative_sides():
    a, b, c = -6, -8, -10
    with pytest.raises(AssertionError):
        perimeter(a, b, c)
