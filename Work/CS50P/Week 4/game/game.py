import random
import sys

# without using separate functions

while True:
        try:
            lvl = int(input("Level: "))
            if lvl < 0:
                raise ValueError
            else:
                r = random.randint(1, lvl)
                while True:
                            try:
                                guess = int(input("Guess: "))
                                if guess < 0:
                                    raise ValueError
                                elif guess > r:
                                    print("Too large!")
                                elif guess < r:
                                    print("Too small!")
                                else:
                                    sys.exit("Just right!")
                            except ValueError:
                                     print("Only positive integers!")

        except ValueError:
            print("Only positive integers!")



# with the use of separate functions

"""
def main():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl < 0:
                raise ValueError
            else:
                lvl = game(lvl)
        except ValueError:
            print("Only positive integers!")



def game(n):
    r = random.randint(1, n)
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 0:
                raise ValueError
            elif guess > r:
                print("Too large!")
            elif guess < r:
                print("Too small!")
            else:
                sys.exit("Just right!")
        except ValueError:
            print("Only positive integers!")


main()
"""











