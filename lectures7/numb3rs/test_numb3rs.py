from numb3rs import validate


def main():
    test_validate()


def test_ip_type():
    assert validate(r"cat") == False
    assert validate(r"cat.225.1.2") == False
    assert validate(r"cat.dog.225.1") == False


def test_ip_range():
    assert validate(r"127.0.0.1") == True
    assert validate(r"1.2.3.4") == True
    assert validate(r"512.512.512.512") == False
    assert validate(r"1.2.3.1000") == False
    assert validate(r"275.3.6.28") == False
    assert validate(r"255.1.266.266") == False


def test_ip_format():
    assert validate(r"255.255.255.255") == True
    assert validate(r"255") == False
    assert validate(r"255.255") == False
    assert validate(r"255.255.255") == False


if __name__ == "__main__":
    main()
