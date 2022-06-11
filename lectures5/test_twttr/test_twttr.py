from twttr import shorten


def main():
    test_twttr_char_case()
    test_twttr_number_case()
    test_twttr_punctuation()


def test_twttr_char_case():
    # test upper or lower case
    assert shorten("twitter") == "twttr"
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("TwITTer") == "TwTTr"


def test_twttr_number_case():
    # test number case
    assert shorten('1234') == '1234'
    assert shorten('0000') == '0000'


def test_twttr_punctuation():
    # test puncation case
    assert shorten('!,.?#$%') == '!,.?#$%'


if __name__ == "__main__":
    main()
