# get greeting
greeting = input("Greeting: ").strip().lower()

# if "hello" in gretting, output $0
if "hello" in greeting:
    print("$0")
# elif start with "h" , but not "hello", output $20
elif greeting[0] == "h":
    print("$20")
# none of above, output $100
else:
    print("$100")