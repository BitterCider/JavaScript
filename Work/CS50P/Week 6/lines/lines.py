import sys

numline = 0
try:
    if len(sys.argv) > 2:
        sys.exit("Too many cmd-line arguments")
    if len(sys.argv) < 2:
        sys.exit("Too few cmd-line arguments")
    if not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    if len(sys.argv) == 2:
        with open(f"{sys.argv[1]}", "r") as file:
            lines = file.readlines()
            
        for line in lines:
            line = line.lstrip()
            if not line.startswith("#") and line.strip():
                numline += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(numline)
