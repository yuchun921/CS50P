# get user input
def main():
    msg = input("type: ")
    playback_msg = playback(msg)
    print(playback_msg)


# trun ... replace space
def playback(msg):
    playback_msg = msg.replace(" ", "...")
    return playback_msg


# output
main()