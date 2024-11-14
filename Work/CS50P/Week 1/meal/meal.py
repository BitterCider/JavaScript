# With 12-hour clock support, a little messy but w/e
def main():

    mtime = input("What time is it? ")

    if "a.m." in mtime or "p.m." in mtime:
        timenum12, period  = convert12(mtime)


        if (period == "a.m.") and (7 <= timenum12 <= 8):
            print("breakfast time")

        elif (period == "p.m." and 12 <= timenum12) or (period == "p.m." and timenum12 <= 1):
            print("lunch time")

        elif (period == "p.m." and 6 <= timenum12 <= 7):
            print("dinner time")

    else:
        mealtime = convert(mtime)

        if (7 <= mealtime <= 8):
             print("breakfast time")

        if (12 <= mealtime <= 13):
             print("lunch time")

        if (18 <= mealtime <= 19):
             print("dinner time")

def convert12(time12):
    num, period = (time12.split(" "))
    l, r = (num.split(":"))
    q = float(l)
    e = float(r)
    twelvehour = (q + (e/60))
    return (twelvehour, period)



def convert(time):
    x, y = (time.split(":"))
    h = float(x)
    m = float(y)
    timenum = (h + (m/60))
    return (timenum)


if __name__ == "__main__":
    main()
