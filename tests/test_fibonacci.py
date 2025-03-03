from ..sequence.fibonacci import fibonacci
import pytest


def test_fibonacci():
    assert fibonacci(1) == 0
    assert fibonacci(2) == 1
    assert fibonacci(5) == 3
    assert fibonacci(10) == 34


def test_fibonacci_invalid():
    with pytest.raises(ValueError):
        fibonacci(0)
