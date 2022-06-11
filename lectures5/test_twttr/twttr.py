def main():
    msg = input("Input: ")
    result = shorten(msg)
    print(f"Output: {result}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]
    msg = ""
    for c in word:
        # check if char is vowels
        if c.lower() in vowels:
            continue
        msg += c

    return msg


if __name__ == "__main__":
    main()
