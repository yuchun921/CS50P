amount_due = 50
while amount_due > 0:
    # print amount due
    print(f"amount_due: {amount_due}")

    # user input coint
    coin = int(input("Insert Coin: "))

    # validate 25, 10, 5
    if coin in [25, 10, 5]:
        # amount_due subtract coin
        amount_due -= coin

# cal change_owned
change_owned = abs(amount_due)
# output
print(f"Change owed: {change_owned}")
