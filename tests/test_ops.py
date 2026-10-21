import pytest

from calc.ops import add, subtract, multiply, divide


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-1, -4) == -5


def test_add_mixed():
    assert add(-2, 7) == 5


def test_subtract_positive():
    assert subtract(10, 4) == 6


def test_subtract_negative_result():
    assert subtract(3, 8) == -5


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_multiply_negative():
    assert multiply(-2, 6) == -12


def test_divide_even():
    assert divide(10, 2) == 5


def test_divide_fraction():
    assert divide(1, 4) == 0.25


def test_divide_by_zero():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1, 0)
