def main():
    short = input("Input: ")
    print(shorten(short))


def shorten(word):
    out = ""
    Omitted = "AEOUIaeoui"
    for i in word:
        if i not in Omitted:
            out += i

    return out


if __name__ == "__main__":
    main()
