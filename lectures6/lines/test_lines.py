from lines import check_arguments, check_space_comment
import pytest


def main():
    # call test function
    test_argu()
    test_space_comment()


def test_argu():
    # argv length less than 2
    with pytest.raises(SystemExit):
        check_arguments(["line.py"])
    # argv length greater than 2
    with pytest.raises(SystemExit):
        check_arguments(["line.py", "a.py", "b.py"])
    # not a python file
    with pytest.raises(SystemExit):
        check_arguments(["line.py", "a.txt"])


def test_space_comment():
    # check comment
    assert check_space_comment("    # comment") == True
    # chekc space line
    assert check_space_comment("  ") == True
    # check normal situation
    assert check_space_comment("line_count = 0") == False


if __name__ == "__main__":
    main()
