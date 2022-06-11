# menu dictionary
MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():
    # total price
    total = 0

    while True:
        try:
            # get user input
            item: str = input("Item: ").title()
        # ctrl+d will stop code
        except EOFError:
            print()
            break
        # check input in menu, then cal price
        if item in MENU:
            total += MENU[item]
            print(f"Total: ${total:.2f}")


if __name__ == "__main__":
    main()
