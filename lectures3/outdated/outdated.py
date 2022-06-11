# months values
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    # user input
    date = input("Date: ").strip()
    # use "/" to split
    if "/" in date:
        month, day, year = date.split("/")
    # replace "," to "space", then use "space" to split
    elif "," in date:
        date = date.replace(",", "")
        month, day, year = date.split(" ")
        # valid month, and get integer
        if month in months:
            month = months.index(month) + 1
    else:
        continue
    # error handle, if month or day not integer and not valid value
    try:
        if (1 > int(month) or int(month) > 12) or (1 > int(day) or int(day) > 31):
            continue
        else:
            break
    except ValueError:
        continue

print(f"{year}-{int(month):02}-{int(day):02}")
