import random


def main():
    # get level
    level: int = get_level()
    # get score
    score: int = start_cal(level)
    # output
    print(f"Score: {score}")


def get_level() -> int:
    # get level
    while True:
        try:
            # user input
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                return level
        except ValueError:
            pass


def generate_integer(level):
    # get topic x y
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y


def answer_correct(x, y):
    # get anwer correct or not
    count = 1
    while count <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x+y):
                return True
            else:
                count += 1
                print("EEE")
        except:
            count += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False


def start_cal(level):
    # start cal topic and get score
    score = 0
    for _ in range(0, 10):
        x, y = generate_integer(level)
        result = answer_correct(x, y)
        if result:
            score += 1
    return score


if __name__ == "__main__":
    main()
