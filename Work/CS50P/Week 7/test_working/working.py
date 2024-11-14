import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):                 # g1              g2         g3              g4              g5     g6
    if matches := re.search(r"(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[0-9])(:[0-5][0-9])? (AM|PM)", s):
            hr_start, hr_fin = map(int, matches.group(1, 4))
            if matches.group(3) == "PM":
                if hr_start != 12:
                    hr_start = (hr_start + 12)

            if matches.group(6) == "PM":
                if hr_fin != 12:
                    hr_fin = (hr_fin + 12)

            if matches.group(3) == "AM":
                hr_start = hr_start % 12

            if matches.group(6) == "AM":
                hr_fin = hr_fin % 12

    else:
        raise ValueError

    if not matches.group(2) or not matches.group(5):
        format24 = f"{hr_start:02}:00 to {hr_fin:02}:00"
    elif matches.group(2) or matches.group(5):
            format24 = f"{hr_start:02}{matches.group(2)} to {hr_fin:02}{matches.group(5)}"
    return format24






if __name__ == "__main__":
    main()
