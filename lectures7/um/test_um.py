from um import count


def main():
    test_wrong_word()
    test_upper()

def test_wrong_word():
    assert count("sum") == 0
    assert count("jump") == 0
    assert count("Hey, um!") == 1

def test_upper():
    assert count("Hey, UM!") == 1
    assert count("Um, thanks, um...") == 2

if __name__ == "__main__":
    main()
