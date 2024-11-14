months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        date = input("Date: ")
        if "/" in date:
            a, b, c = date.split("/")
            m = int(a)
            d = int(b)
            y = int(c)
            if m > 12 or d > 31:
                print("Only M/D/Y Format")
                raise SyntaxError
            else:
                print(f"{y}-{m:02}-{d:02}")
                break
            
        elif "," in date:

            a, b, c = date.split(" ")
            b = b.replace(",", "")
            d = int(b)
            y = int(c)
            for i in months:
                if a == i:
                    a = str(months.index(i)+1)
            m = int(a)
            if d > 31 or m > 12:
                raise ValueError

            print(f"{y}-{m:02}-{d:02}")
            break

    except (ValueError, SyntaxError):
        print(end="")





