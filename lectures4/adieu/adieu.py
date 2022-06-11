import inflect
p = inflect.engine()

names = []
while True:
    try:
        # get user input
        name: str = input("Name: ").title()
    # ctrl+d will stop code
    except EOFError:
        print()
        break
    # check name exists
    if name not in names:
        names.append(name)

# conver input to desired format
result = p.join(names)
print(f"Adieu, adieu, to {result}")