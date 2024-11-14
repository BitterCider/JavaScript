import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        a, b, c, d = map(int, ip.split("."))
        if max(a, b, c, d) <= 255:
            return True
    return False


if __name__ == "__main__":
    main()
