#  get user unput
name = input("What's name? ")

# check each char
for char in name:
    # handle if char is upper
    if char.isupper():
        print(f"_{char.lower()}", end="")
    # char not upper
    else:
        print(char, end="")
# print a new line
print()