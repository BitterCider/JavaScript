menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

bill = 0

while True:
    try:
        order = (input("Item: ").title())
        bill += menu[order]
        print("${:.2f}".format(bill))
    except KeyError:
        print("This is Felipe's Taqueria Sir")
    except EOFError:
        break





