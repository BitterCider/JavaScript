def main():
    fraction = input("Fraction: ")
    try:
        gas = convert(fraction)
    except (ValueError, ZeroDivisionError):
        print("Fractions only!")
        main()
    else:
        gas = gauge(gas)
        print(gas)

def convert(fraction):
    x, y = (int(i) for i in fraction.split("/"))
    volume = round(float((x / y) * 100))
    if x > y:
        raise ValueError
    return volume

def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"

if __name__ == "__main__":
    main()
