import re


def main():
    # output
    print(count(input("Text: ")))


def count(s):
    # find "um" in s, save in um list
    um: list = re.findall(r"\b\W*um\W*", s, re.IGNORECASE)
    # return len(um)
    return len(um)


if __name__ == "__main__":
    main()
