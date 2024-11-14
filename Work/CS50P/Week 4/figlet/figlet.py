from pyfiglet import Figlet
figlet = Figlet()
fonts = figlet.getFonts()
import sys
import random
random_font = random.choice(fonts)

if len(sys.argv) > 3:
        sys.exit("Too many arguments")

elif len(sys.argv) == 1:
        UserInput = input("Input: ")
        figlet.setFont(font=random_font)
        print(figlet.renderText(UserInput))

elif len(sys.argv) >= 2 and "-f" != sys.argv[1] and "--font" != sys.argv[1]:
        sys.exit("Type either -f or --font")

elif len(sys.argv) == 3:
        if sys.argv[2] not in fonts:
                sys.exit("Please choose a valid font")
        else:
                UserInput = input("Input: ")
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(UserInput))






