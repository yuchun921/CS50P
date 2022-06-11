def main():
    # get file name
    file_name = input("File name: ").strip().lower()
    print(extension(file_name))


def extension(file_name):
    # check file extension type, and categorize
    # gif: image/gif
    if ".gif" in file_name:
        return "image/gif"
    # jpeg and jpg: image/jpeg
    elif ".jpeg" in file_name:
        return "image/jpeg"
    elif ".jpg" in file_name:
        return "image/jpeg"
    # png: image/png
    elif ".png" in file_name:
        return "image/png"
    # pdf: application/pdf
    elif ".pdf" in file_name:
        return "application/pdf"
    # txt: text/plain
    elif ".txt" in file_name:
        return "text/plain"
    # zip: application/zip
    elif ".zip" in file_name:
        return "application/zip"
    # none of above: application/octet-stream
    else:
        return "application/octet-stream"


# output
main()
