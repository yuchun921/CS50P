import re

email = input("What's your email? ").strip()

if re.search(".+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")