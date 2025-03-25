import pytest
from main import factorials


def test_factorial_zero():
    result = list(factorials(0))
    assert result == [1]


def test_factorial_positive():
    result = list(factorials(5))
    assert result == [1, 2, 6, 24, 120]


def test_factorial_negative():
    result = list(factorials(-1))
    assert result == []


def test_factorial_fraction():
    with pytest.raises(TypeError):
        list(factorials(5.5))
