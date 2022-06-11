# ready for save input
grocery: dict = {}

while True:
    try:
        # get user input
        item: str = input().upper()
    except EOFError:
        print()
        break
    # check input in grocery or not, then cal counts
    if item in grocery:
        grocery[item] += 1
    else:
        grocery[item] = 1

# sorted
for item in sorted(grocery):
    print(f"{grocery[item]} {item}")
