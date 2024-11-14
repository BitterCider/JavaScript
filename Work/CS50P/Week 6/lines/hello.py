import csv
import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments ")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments ")
elif sys.argv[1].endswith(".csv") == False:
    sys.exit("Not a CSV file")


try:
    file = open(sys.argv[1])
    to_write = open(sys.argv[2], "w")
except FileNotFoundError:
    sys.exit("File does not exist")


students = []

reader = csv.DictReader(file)

for row in reader:
    last, first = row["name"].rstrip().split(",")
    house = row["house"]
    students.append({"first": first, "last": last, "house": house})


writer = csv.DictWriter(to_write, fieldnames=["first", "last", "house"])
writer.writeheader()

for student in sorted(students, key=lambda student: student["first"]):
    writer.writerow(
        {"first": student["first"], "last": student["last"], "house": student["house"]}
    )
