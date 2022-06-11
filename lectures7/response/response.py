from validator_collection import validators


def main():
    # user input
    email_addr = input("What's your email address? ")
    # try valid input
    try:
        validators.email(email_addr)
        print("Valid")
    # invalid situation
    except:
        print("Invalid")


if __name__ == "__main__":
    main()
