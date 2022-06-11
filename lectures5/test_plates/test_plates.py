from plates import is_valid


def main():
    # call test func
    test_length()
    test_isalpha()
    test_number_at_middle()
    test_first_num_zero()
    test_punctuation()


def test_length():
    # Plates may contain a maximum of 6 characters and a minimum of 2 characters.
    assert is_valid("OUTATIME") == False
    assert is_valid("CS50") == True
    assert is_valid("CS") == True
    assert is_valid("CS1234") == True
    assert is_valid("C") == False


def test_isalpha():
    # All vanity plates must start with at least two letters.
    assert is_valid("CS") == True
    assert is_valid("C1") == False
    assert is_valid("1C") == False
    assert is_valid("11") == False


def test_number_at_middle():
    # Numbers cannot be used in the middle of a plate; they must come at the end.
    assert is_valid("CS50") == True
    assert is_valid("CS50CS") == False
    assert is_valid("C5S0C") == False


def test_first_num_zero():
    # The first number used cannot be a '0'.
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("PI3.14") == False


def test_punctuation():
    # No periods, spaces, or punctuation marks are allowed.
    assert is_valid("CS50") == True
    assert is_valid("CS5!") == False
    assert is_valid("CS5,") == False


if __name__ == "__main__":
    main()
