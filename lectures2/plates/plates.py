def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    # Plates may contain a maximum of 6 characters and a minimum of 2 characters.
    if len(plate) > 6 or len(plate) < 2:
        return False

    # All vanity plates must start with at least two letters.
    if plate[0:2].isalpha() is False:
        return False

    first_nums = True
    for i in range(len(plate)):
        # No periods, spaces, or punctuation marks are allowed.
        if plate[i].isalnum() is False:
            return False

        # Numbers cannot be used in the middle of a plate; they must come at the end.
        if plate[i].isdigit() and plate[i:].isdigit() is False:
            return False

        # The first number used cannot be a '0'.
        if plate[i].isalpha() is False and first_nums is True:
            if plate[i] == "0" and first_nums is True:
                return False
            else:
                first_nums = False
    return True


if __name__ == "__main__":
    main()