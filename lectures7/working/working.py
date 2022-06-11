import re


def main():
    # output
    print(convert(input("Hours: ")))


def convert(s):
    # check format
    if correct_format := re.search(
            r"^([0-9][0-2]*):*([0-5][0-9])* ([A|P]M) to ([0-9][0-2]*):*([0-5][0-9])* ([A|P]M)$", s):

        # check hour less than 12
        if int(correct_format.group(1)) > 12 or int(correct_format.group(4)) > 12:
            raise ValueError

        # get correct format
        # first time
        first_time = new_format(correct_format.group(
            1), correct_format.group(2), correct_format.group(3))
        # last time
        last_time = new_format(correct_format.group(
            4), correct_format.group(5), correct_format.group(6))
        return f"{first_time} to {last_time}"
    else:
        raise ValueError


def new_format(hour, mins, am_pm):
    # PM situation
    if am_pm == "PM":
        if hour == "12":
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    # AM situation
    else:
        if hour == "12":
            new_hour = 0
        else:
            new_hour = int(hour)
    # got mins
    if mins is None:
        new_min = '00'
        new_time = f"{new_hour:02}:{new_min}"
    else:
        new_time = f"{new_hour:02}:{mins}"
    return new_time


if __name__ == "__main__":
    main()
