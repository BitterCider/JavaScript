import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if matches := re.search(
        r"src\=(\"https?://(?:www\.)?youtube\.com/embed/(\w+)\")", s):
        url = re.sub(s, "https://youtu.be/" + matches.group(2), s)
        return url


if __name__ == "__main__":
    main()
