## operator
# x = 999.444
# y = 1.674
# z = x + y

# print(f"{z:.2f}")


def main():
    x = int(input("What's x? "))
    print(f"x squared is {square(x)}")


def square(n: int):
    return n * n


main()
