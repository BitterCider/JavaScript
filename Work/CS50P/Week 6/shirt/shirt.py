from PIL import Image, ImageOps
from os.path import splitext
import sys

exten_list = [".jpeg", ".png", ".jpg"]


def main():
    if check_arg():
        try:
            before_muppets = Image.open(f"{sys.argv[1]}")
            shirt = Image.open("shirt.png")
        except FileNotFoundError:
            sys.exit("Input does not exist")
    fit_muppets = ImageOps.fit(before_muppets, (600, 600))
    shirt = ImageOps.fit(shirt, (600, 600))
    fit_muppets.paste(shirt, shirt)
    fit_muppets.save(f"{sys.argv[2]}")


def check_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few cmd-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many cmd-line arguments")
    Input = splitext(sys.argv[1].lower())
    Output = splitext(sys.argv[2].lower())
    if check_ex(Input[1]) == False:
        sys.exit("Invalid input")
    if check_ex(Output[1]) == False:
        sys.exit("Invalid output")
    if Input[1] != Output[1]:
        sys.exit("Input and output extensions not the same")
    else:
        return True


def check_ex(ex):
    if ex not in exten_list:
        return False
    else:
        return True


if __name__ == "__main__":
    main()
