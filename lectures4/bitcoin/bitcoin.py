import requests
from sys import argv, exit

# not give command-line argument
if len(argv) != 2:
    exit("Missing command-line argument")
# command-line argument is not a float
try:
    n = float(argv[1])
except ValueError:
    exit("Command-line argument is not a number")

# get data through bitcoin API
try:
    response = requests.get(
        "https://api.coindesk.com/v1/bpi/currentprice.json")
    rate_float = response.json()["bpi"]["USD"]["rate_float"]
    # calculate total
    total = rate_float * n
    print(f'${total:,.4f}')
except requests.RequestException as req_error:
    exit(req_error)
