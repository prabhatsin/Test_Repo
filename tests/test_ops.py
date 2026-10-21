import pytest

from calc.ops import add, subtract, multiply, divide


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -4) == -5


def test_add_mixed():
    assert add(10, -3) == 7


def test_subtract_positive():
    assert subtract(5, 3) == 2


def test_subtract_negative_result():
    assert subtract(3, 5) == -2


def test_multiply_positive():
    assert multiply(4, 3) == 12


def test_multiply_by_zero():
    assert multiply(7, 0) == 0


def test_multiply_negative():
    assert multiply(-2, 3) == -6


def test_divide_exact():
    assert divide(10, 2) == 5


def test_divide_fraction():
    assert divide(1, 4) == 0.25


def test_divide_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1, 0)
