"""
x = int(input("What's x? "))
print(f"x is {x}")
"""

# -----------------------------------------------------------------
# Traceback (most recent call last):
#   File "/workspaces/70684698/cx50p/lectures3/number.py", line 1, in <module>
#     x = int(input("What's x? "))
# ValueError: invalid literal for int() with base 10: 'a'
# -----------------------------------------------------------------



''' try '''

# x = input("What's x? ")
# try:
#     x = int(x)
# except ValueError:
#     print(f"{x} is not integer")
# else:
#     print(f"x is {x}")


# while True:
#     try:
#         x = int(input("What's x?"))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

''' build a fuction '''
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")
            pass

if __name__ == "__main__":
    main()