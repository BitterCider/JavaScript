def main():
    Greeting = value(input("Greeting: "))
    print(f"${Greeting}")


def value(greeting):
    greeting = greeting.lower().lstrip()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()