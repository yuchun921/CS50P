import sys


def main():
    # check sys.argv
    file = check_arguments(sys.argv)
    lines = file.readlines()
    line_count = 0
    for line in lines:
        if check_space_comment(line):
            continue
        line_count += 1
    print(line_count)


def check_arguments(argv):
    # check too few arguments
    if len(argv) < 2:
        sys.exit("Too few command-line arguments")
    # check too many arguments
    if len(argv) > 2:
        sys.exit("Too many command-line arguments")
    # check it is python file
    if ".py" not in argv[1]:
        sys.exit("Not a Python file")
    # check python file exit
    try:
        file = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("File does not exist")
    return file


def check_space_comment(line):
    if line.strip().startswith("#") or line.isspace():
        return True
    return False


if __name__ == "__main__":
    main()
