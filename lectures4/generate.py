import random

"""
random.choice(seq)
    Return a random element from the non-empty sequence seq. If seq is empty, raises IndexError.
"""
coin = random.choice(["heads", "tails"])
print(coin)


"""
random.randint(a, b)
    Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
"""
number = random.randint(1, 11)
print(number)


"""
random.shuffle(x[, random])
    Shuffle the sequence x in place.
"""
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
