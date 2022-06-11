import re

name = input("What's your name? ").strip()

if matches := re.search("^(.+), ?(.+)$", name):
    name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")