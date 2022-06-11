from math import floor


def cal_fuel(prompt):
    # loop for remind the user again
    while True:
        # get user input
        fuel: str = input(prompt)
        try:
            # split: /
            x, y = fuel.split("/")

            # X and Y must be integer
            x = int(x)
            y = int(y)

            # X must less than or equal to Y, and Y can not be 0
            # trun to decimal
            decimal = x / y
            # check decimal valid => it should less than 1
            if decimal <= 1:
                return decimal

        except (ValueError, ZeroDivisionError):
            pass


def turn_percentage(decimal: float) -> int:
    return round(decimal * 100)


def main():
    # get decimal
    decimal: float = cal_fuel("Fuel: ")
    # turn decimal to percentage%
    percentage: int = turn_percentage(decimal)

    # less than 1, print E
    if percentage <= 1:
        print("E")
    # more than 99, print F
    elif percentage >= 99:
        print("F")
    # none of above
    else:
        print(f"{percentage}%")


if __name__ == "__main__":
    main()
