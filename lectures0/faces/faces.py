def main():
    # get user input
    msg = input("msg: ")
    # convert
    face_msg = convert_face(msg)
    # output
    print(face_msg)


def convert_face(msg):
    # conver :) and :(
    smile_cry_face = msg.replace(":)", "🙂").replace(":(", "🙁")
    return smile_cry_face


main()
