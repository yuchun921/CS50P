from seasons import delta, words, date_format
from datetime import date
import pytest


def main():
    test_date_format()
    test_delta()
    test_words()


def test_date_format():
    assert date_format("1994-09-21") == 14580000
    with pytest.raises(SystemExit):
        date_format("1994,09,21")


def test_delta():
    assert delta(date.fromisoformat("1994-09-21")) == 14580000


def test_words():
    assert words(
        14580000) == "fourteen million, five hundred and eighty thousand"


if __name__ == "__main__":
    main()
