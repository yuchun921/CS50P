from datetime import date
import sys
import inflect


def main():
    # user input
    birthday = input("Date of Birth: ")
    # get mins
    mins = date_format(birthday)
    # output
    print(f"{words(mins).capitalize().replace(' and','')} minutes")


def date_format(b_day):
    # valid user input is correct format
    try:
        d = date.fromisoformat(b_day)
    except ValueError:
        sys.exit("Invalid date")
    else:
        return delta(d)


def delta(d):
    # get minutes
    day = date.today() - d
    return day.days * 24 * 60


def words(n):
    # turn to number to words
    p = inflect.engine()
    return p.number_to_words(n)


if __name__ == "__main__":
    main()
