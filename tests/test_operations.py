# tests/test_operations.py
import pytest
from app.operations import add, subtract, multiply, divide


# ---------- ADD ----------
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (-1, 1, 0),
    (0, 0, 0),
    (2.5, 3, 5.5),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


# ---------- SUBTRACT ----------
@pytest.mark.parametrize("a, b, expected", [
    (5, 3, 2),
    (5.5, 2, 3.5),
    (0, 5, -5),
])
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected


# ---------- MULTIPLY ----------
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 6),
    (2.5, 4, 10.0),
    (0, 100, 0),
])
def test_multiply(a, b, expected):
    assert multiply(a, b) == expected


# ---------- DIVIDE ----------
@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2.0),
    (5.5, 2, 2.75),
    (9, 3, 3.0),
])
def test_divide(a, b, expected):
    assert divide(a, b) == expected


# ---------- DIVIDE BY ZERO (critical edge case) ----------
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(5, 0)
