def main():
    fraction: str = input("Fuel: ")
    percentage = convert(fraction)
    # turn decimal to percentage%
    print(gauge(percentage))


def convert(fraction):
    # loop for remind the user again
    while True:
        # get user input
        try:
            # split: /
            x, y = fraction.split("/")

            # X and Y must be integer
            x = int(x)
            y = int(y)

            # X must less than or equal to Y, and Y can not be 0
            # trun to decimal
            decimal = x / y
            # check decimal valid => it should less than 1
            if decimal <= 1:
                return round(decimal * 100)
            fraction: str = input("Fuel: ")
            continue

        except (ValueError, ZeroDivisionError):
            raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    # more than 99, print F
    elif percentage >= 99:
        return "F"
    # none of above
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()