def main():
    greeting = input("Greeting: ")
    result = value(greeting)
    print(f"${result}")


def value(greeting):
    greet = greeting.strip().lower()
    # if "hello" in gretting, output $0
    if "hello" in greet:
        return 0
    # elif start with "h" , but not "hello", output $20
    elif greet[0] == "h":
        return 20
    # none of above, output $100
    else:
        return 100


if __name__ == "__main__":
    main()
