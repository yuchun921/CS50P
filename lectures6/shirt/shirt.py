import sys
from os.path import splitext
from PIL import Image, ImageOps


VALID_FILE_EXTENSION = [".jpg", ".jpeg", ".png"]


def main():
    check_argument()

    # open image
    try:
        image_file = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")
    # open shirt
    shirt = Image.open("shirt.png")
    # get shirt size
    size = shirt.size
    # # resize muppet image to fit shirt
    muppet_resize = ImageOps.fit(image_file, size)
    # paste shirt on image
    muppet_resize.paste(shirt, shirt)
    # save final photo
    muppet_resize.save(sys.argv[2])


def check_argument():
    # check sys.argv length
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # get sys.argv file extension
    file1 = sys.argv[1].lower()
    file2 = sys.argv[2].lower()
    file1_extention = splitext(file1)
    file2_extention = splitext(file2)

    # check file1 and fiel2 are both ".jpg" or ".jpeg" or ".png"
    if not file1_extention[1] in VALID_FILE_EXTENSION or not file2_extention[1] in VALID_FILE_EXTENSION:
        sys.exit("Invalid input")

    # chekc file1 and file2 extension of are the smae
    if file1_extention[1] != file2_extention[1]:
        sys.exit("Input and output have different extensions")


if __name__ == "__main__":
    main()
