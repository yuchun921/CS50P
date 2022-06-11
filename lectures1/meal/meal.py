def main():
    time = input("Time: ")
    print(convert(time))


def convert(time):
    hour, _ = time.split(":")
    if 7 <= int(hour) <= 8:
        return "breakfast time"
    elif 12 <= int(hour) <= 13:
        return "lunch time"
    elif 18 <= int(hour) <= 19:
        return "dinner time"


if __name__ == "__main__":
    main()