import re

def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r"(?<![a-z])um(?![a-z])", s, re.IGNORECASE))


if __name__ == "__main__":
    main()
