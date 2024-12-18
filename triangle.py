from math import sqrt

def perimeter(a, b, c):
    if a < 0 or b < 0 or c < 0:
        raise AssertionError("Стороны не могут быть отрицательными")
    return a + b + c

def area(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        raise AssertionError("Стороны не могут быть отрицательными или равными нулю")
    if a + b <= c or a + c <= b or b + c <= a:
        raise AssertionError("Сумма двух сторон должна быть больше третьей")
    x = (a + b + c) / 2
    return sqrt(x * (x - a) * (x - b) * (x - c))
