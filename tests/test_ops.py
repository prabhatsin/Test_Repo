import pytest

from calc.ops import add, divide, multiply, subtract


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-4, -6) == -10


def test_add_mixed_signs():
    assert add(10, -3) == 7


def test_subtract_positive_numbers():
    assert subtract(10, 4) == 6


def test_subtract_to_negative():
    assert subtract(3, 8) == -5


def test_multiply_positive_numbers():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(7, 0) == 0


def test_multiply_negative_numbers():
    assert multiply(-2, 5) == -10


def test_divide_evenly():
    assert divide(10, 2) == 5


def test_divide_returns_float():
    assert divide(7, 2) == 3.5


def test_divide_by_zero_raises():
    with pytest.raises(ValueError, match="cannot divide by zero"):
        divide(1, 0)
