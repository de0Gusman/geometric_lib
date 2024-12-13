import pytest
from calculate import calc
from math import pi


def test_area_of_circle():
    figure = 'circle'
    operation = 'area'
    dimensions = [2]
    result = calc(figure, operation, dimensions)
    assert result == 4 * pi

def test_area_of_square():
    figure = 'square'
    operation = 'area'
    dimensions = [2]
    result = calc(figure, operation, dimensions)
    assert result == 4

def test_area_of_triangle():
    figure = 'triangle'
    operation = 'area'
    dimensions = [6, 8, 10]
    result = calc(figure, operation, dimensions)
    assert result == 24

def test_perimeter_of_circle():
    figure = 'circle'
    operation = 'perimeter'
    dimensions = [2]
    result = calc(figure, operation, dimensions)
    assert result == 4 * pi

def test_perimeter_of_square():
    figure = 'square'
    operation = 'perimeter'
    dimensions = [2]
    result = calc(figure, operation, dimensions)
    assert result == 8

def test_perimeter_of_triangle():
    figure = 'triangle'
    operation = 'perimeter'
    dimensions = [6, 8, 10]
    result = calc(figure, operation, dimensions)
    assert result == 24

def test_invalid_figure():
    figure = 'hexagon'
    operation = 'area'
    dimensions = [2]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_invalid_function():
    figure = 'circle'
    operation = 'diagonal'
    dimensions = [2]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_invalid_size():
    figure = 'square'
    operation = 'area'
    dimensions = [2, 3]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_negative_size_area_circle():
    figure = 'circle'
    operation = 'area'
    dimensions = [-2]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_negative_size_area_square():
    figure = 'square'
    operation = 'area'
    dimensions = [-2]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_negative_size_area_triangle():
    figure = 'triangle'
    operation = 'area'
    dimensions = [-6, -8, -10]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_negative_size_perimeter_circle():
    figure = 'circle'
    operation = 'perimeter'
    dimensions = [-2]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_negative_size_perimeter_square():
    figure = 'square'
    operation = 'perimeter'
    dimensions = [-2]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_negative_size_perimeter_triangle():
    figure = 'triangle'
    operation = 'perimeter'
    dimensions = [-6, -8, -10]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)

def test_invalid_size_for_triangle():
    figure = 'triangle'
    operation = 'area'
    dimensions = [2, 3, 12]
    with pytest.raises(AssertionError):
        calc(figure, operation, dimensions)
