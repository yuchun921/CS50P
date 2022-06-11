import re
import sys


def main():
    # output
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # validate IP correct
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        list_numbers = ip.split(".")
        # check each num between 0 and 255
        for num in list_numbers:
            if int(num) > 255 or int(num) < 0:
                return False
        return True
    return False


if __name__ == "__main__":
    main()
