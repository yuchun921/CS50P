# name = input("What's your name? ")

# with open("name.csv","a", newline="") as file:
#     file.write(f"{name}\n")

names = []
# TODO: read
with open("name.csv", "r") as file:
    for line in file:
        names.append(line)

