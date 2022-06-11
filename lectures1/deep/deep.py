def main():
    # get user input
    msg = input("Say something: ").strip().lower()
    # output
    print(deep(msg))


def deep(msg):
    # check input
    match msg:
        case "42" | "forty two" | "forty-two":
            return "Yes"
        case _:
            return "No"


main()


"""
if msg.strip().lower() in ["42", "forty two", "forty-two"]:
    print("Yes")
else:
    print("No")
"""