import pytest

from is_even import divide, is_even


def test_is_even_when_number_is_even_return_true():
    assert is_even(2) is True


def test_is_even_when_number_is_even_return_false():
    assert is_even(3) is False


def test_divide_when_return_exception_error():
    with pytest.raises(ZeroDivisionError):
        divide(2, 0)
