import emoji as emo

# get user input
msg = input("Input: ")
print(f"Output: {emo.emojize(msg, language='alias')}")
