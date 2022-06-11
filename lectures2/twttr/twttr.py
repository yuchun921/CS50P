# get user input
msg = input("Input: ")

# output
print("Output: ", end="")

# save a, e, i, o, u to list
vowels = ["a", "e", "i", "o", "u"]

# loop each char in msg
for c in msg:
    # check if char is vowels
    if c.lower() in vowels:
        continue
    # if not vowels, then print it.
    print(c, end="")
# new line
print()
