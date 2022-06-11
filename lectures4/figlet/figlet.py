# import figlet
import random
from sys import argv, exit

from pyfiglet import Figlet

figlet = Figlet()

# get available fonts
available_fonts = figlet.getFonts()

# check argv
if len(argv) not in [1, 3]:
    exit("Invalid usage")
elif len(argv) > 1 and argv[1] not in ["-f", "-font"]:
    exit("Invalid usage")
elif len(argv) > 1 and argv[2] not in available_fonts:
    exit("Invalid usage")

# get user input
msg = input("Input: ")
# setting font
font_setting = random.choice(available_fonts) if len(argv) == 1 else argv[2]
figlet.setFont(font=font_setting)
# output
print(figlet.renderText(msg))
