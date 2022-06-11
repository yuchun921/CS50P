import re


def main():
    # output
    print(parse(input("HTML: ")))


def parse(s):
    # check <iframe></iframe> in s
    if re.search(r"<iframe(.)*<\/iframe>", s, re.IGNORECASE):
        # check "youtube.com" in s
        if url_pattern := re.search(r"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9_]+)", s):
            result = f"https://youtu.be/{url_pattern.group(1)}"
            return result


if __name__ == "__main__":
    main()
