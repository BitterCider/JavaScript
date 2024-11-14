import random


def main():
    tries = 0
    score = 0
    answer = True
    level = get_level()
    while tries <= 10:
        if answer == True:
            mistake = 0
            try:
                x = generate_integer(level)
                y = generate_integer(level)
                sum = int(input(f"{x} + {y} = "))
                tries += 1
                if sum == (x + y):
                    score += 1
                else:
                    raise ValueError
            except ValueError:
                mistake += 1
                print("EEE")
                answer = False
        if answer == False:
            try:
                sum = int(input(f"{x} + {y} = "))
                if sum == (x + y):
                    score += 1
                    answer = True
                else:
                    raise ValueError
            except ValueError:
                mistake += 1
                print("EEE")
        if mistake == 3:
            print(f"{x} + {y} = {x + y}")
            mistake = 0
            answer = True
        if tries == 10:
            print(f"Score: {score}")
            return None


def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl in [1, 2, 3]:
                return lvl
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
