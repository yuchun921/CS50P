"""
if loop statement:
    please refer to this URL: https://cs50.harvard.edu/python/2022/notes/1/#creating-our-own-parity-function
"""


x = int(input("What's x? "))
y = int(input("What's y? "))

# if statement
if x < y:
    print(f"{x} is less than {y}")
if x > y:
    print(f"{x} is greater than {y}")
if x == y:
    print(f"{x} is equal to {y}")

# if..elif..statement
if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")

# if...elif...else
if x < y:
    print(f"{x} is less than {y}")
elif x > y:
    print(f"{x} is greater than {y}")
else:
    print(f"{x} is equal to {y}")

"""  ------------------------------------------ """

# or
if x != y:
    print(f"{x} is not equal to {y}")
else:
    print(f"{x} is equal to {y}")
