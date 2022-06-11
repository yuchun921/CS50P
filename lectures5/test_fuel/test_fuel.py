from fuel import convert, gauge
import pytest


def main():
    # call test function
    test_convert()
    test_gauge()
    test_zero_division()
    test_value_error()


def test_convert():
    # test convert func
    assert convert("1/4") == 25
    assert convert("1/2") == 50
    assert convert("1/1") == 100
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge():
    # test gauge func
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(100) == "F"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_zero_division():
    # test zero division
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    # test value error
    with pytest.raises(ValueError):
        convert("dog/dogs")


if __name__ == "__main__":
    main()
