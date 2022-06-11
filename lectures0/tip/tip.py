def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


# get dollars and trun float
def dollars_to_float(d):
    dollars = float(d.replace("$", ""))
    return dollars


# get percent and trun float
def percent_to_float(p):
    percent = float(p.replace("%", "")) / 100
    return percent


main()
