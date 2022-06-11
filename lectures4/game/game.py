from random import randint

while True:
    try:
        # setting guess range
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass

# save random number between 1 and level
random = randint(1, level)

while True:
    try:
        # get user guess
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
    except ValueError:
        continue

    # compar guess and random
    if guess > random:
        print("Too large!")
    elif guess < random:
        print("Too small!")
    else:
        print("Just right!")
        break

