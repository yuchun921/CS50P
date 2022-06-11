from tabulate import tabulate
import sys
import csv


def main():
    # check sys argv
    file = check_argument()
    # DictReader
    csv_reader = csv.DictReader(file)
    # output
    print(tabulate(csv_reader, headers="keys", tablefmt="grid"))


def check_argument():
    # check too few arguments
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    # check too many arguments
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # check it is csv file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    # check python file exit
    try:
        file = open(sys.argv[1], "r")
        return file
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
