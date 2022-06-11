from working import convert
import pytest


def main():
    test_wrong()


def test_wrong():
    with pytest.raises(ValueError):
        convert("8 AM - 8 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM - 8:60 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 17 PM")
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("8 PM to 10 AM") == "20:00 to 10:00"
    assert convert("11:30 PM to 8:40 AM") == "23:30 to 08:40"


if __name__ == "__main__":
    main()
