import csv, sys
from tabulate import tabulate
menu = []
try:
    if len(sys.argv) < 2:
        sys.exit("Too few cmd-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many cmd-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    if len(sys.argv) == 2:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
# returns a list of dicts, each dict has the first row (headers) as keys
# while the following rows are values of the corresponding key (header)
# e.g - the first dict in the list will be:
# reader = [{"Sicilian Pizza": "Cheese", "Small": "$25.50", "Large": "$39.95"}]
            for row in reader:
                menu.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")

print(tabulate(menu, headers="keys", tablefmt="grid"))
