import csv, sys
from tabulate import tabulate

students = []

if len(sys.argv) < 3:
    sys.exit("Too few cmd-line arguments")
if len(sys.argv) > 3:
    sys.exit("Too many cmd-line arguments")
elif len(sys.argv) == 3:
    try:
        with open(f"{sys.argv[1]}") as file:
            reader = csv.DictReader(file)
            for row in reader:
                students.append(row)
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(f"{sys.argv[2]}", "w") as file:
        writer = csv.DictWriter(file, fieldnames=("first", "last", "house"))
        writer.writeheader()
        for student in students:
            last, first = (student["name"]).split(",")
            first = first.strip()
            house = student["house"]
            writer.writerow({"first": first, "last": last, "house": house})

table = []

with open(f"{sys.argv[2]}", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        table.append(row)


sorted_students = sorted(table, key=lambda x: x["house"])
print(tabulate(sorted_students, headers="keys", tablefmt="grid"))

