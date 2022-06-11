from bank import value


def main():
    test_hello()
    test_h()
    test_none_of_above()


def test_hello():
    # If the greeting starts with “hello”, output $0
    assert value("Hello") == 0
    assert value("Hello, Newman") == 0


def test_h():
    # If the greeting starts with an “h” (but not “hello”), output $20.
    assert value("How you doing?") == 20
    assert value("Haha") == 20


def test_none_of_above():
    # Otherwise, output $100
    assert value("What's happening?") == 100
    assert value("I'am fine.") == 100


if __name__ == "__main__":
    main()
