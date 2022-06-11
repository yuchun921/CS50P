# get user input
# split to seperate str
x, y, z = input("Expression: ").split()

# calculator
if y == "+":
    result = float(x) + float(z)
elif y == "-":
    result = float(x) - float(z)
elif y == "*":
    result = float(x) * float(z)
else:
    result = float(x) / float(z)

print(result)