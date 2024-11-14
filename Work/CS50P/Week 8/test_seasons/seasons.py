from datetime import date
import inflect
import sys

p = inflect.engine()


def main():
    days = get_delta_words(input("Date of Birth: "))
    print(days)


def get_delta_words(bday):
    try:
        bday = date.fromisoformat(bday)
    except ValueError:
        sys.exit("Invalid date")
    delta = ((date.today() - bday).days) * 24 * 60
    return (f"{p.number_to_words(delta, andword="").capitalize()} minutes")


if __name__ == "__main__":
    main()
