# x = int(input("What's x? "))

# if x % 2 == 0:
#     print("Even")
# else:
#     print("Odd")


# function


def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")


def is_even(num):
    if num % 2 == 0:
        return True
    return False
    ## pythonic:
    # return True if n % 2 == 0 else False
    ## more readable
    # return num % 2 == 0


main()
