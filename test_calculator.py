# test_calculator.py
import os
import pytest
from calculator import add, subtract, multiply, divide, power

DEBUG = os.getenv('DEBUG_MODE', 'false').lower() == 'true'

@pytest.mark.slow
def test_add():
    """Test addition function."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

@pytest.mark.slow
def test_subtract():
    """Test subtraction function."""
    assert subtract(5, 3) == 2
    assert subtract(0, 5) == -5
    assert subtract(-3, -2) == -1

@pytest.mark.slow
def test_multiply():
    """Test multiplication function."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0

@pytest.mark.slow
def test_divide():
    """Test division function."""
    assert divide(8, 2) == 4
    assert divide(9, 3) == 3
    assert divide(-10, 2) == -5

@pytest.mark.slow
def test_divide_by_zero():
    """Test that dividing by zero raises an error."""
    with pytest.raises(ValueError):
        divide(10, 0)

@pytest.mark.slow
def test_power():
    assert power(2, 2) == 4
    assert power(3, 5) == 243
    assert power(4, 7) == 16384
