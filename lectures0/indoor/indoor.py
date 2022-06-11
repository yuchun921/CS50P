# main function
def main():
    say = input("Say: ")
    print(indoor(say))


# turn input to indoor
def indoor(words: str):
    return words.lower()


# call main function
main()
