import sys
import csv


def main():
    # chekc sys.argv
    file = check_argument()

    # csv reader
    csv_reader = csv.DictReader(file)

    # get last, first name
    datas = []
    for row in csv_reader:
        last, first = row["name"].split(",")
        house = row["house"]
        datas.append({"first": first.strip(), "last": last, "house": house})

    # write to after.csv
    new_file_name = sys.argv[2]
    with open(new_file_name, "w", newline='') as f:
        csv_writer = csv.DictWriter(f, fieldnames=["first", "last", "house"])
        csv_writer.writeheader()
        for info in datas:
            csv_writer.writerow(info)


def check_argument():
    # check too few arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    # check too many arguments
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # check it is csv file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
    # check python file exit
    try:
        file = open(sys.argv[1], "r")
        return file
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
