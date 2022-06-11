## not use function
# name = input("What's your name? ").strip().title()
# print(f"Hello {name}")

# function: say hello to someone

def main():
    name = input("Waht's your name? ")
    hello(name)
S
def hello(name: str):
    print(f"Hello, {name}")

main()