
# with import:

import inflect
p = inflect.engine()

name_list = []

while True:
    try:
        name = input("Name: ")
        name_list.append(name)

    except EOFError:
        if len(name_list) == 0:
            print("Type a name")
        else:
            names = p.join(name_list)
            print(f"\nAdieu, adieu, to {names}")
            break

"""
# without import:

name_list = []
adieu = "Adieu, adieu, to"

while True:
    try:
        name = input("Name: ")
        name_list.append(name)

    except EOFError:
        if len(name_list) > 1:
            name1 = name_list[:-1]
            name2 = name_list[-1]
            name1 = ", ".join(name1)
            print(f"{adieu} {name1} and {name2}")
        else:
            print(f"{adieu} {name}")

        break
"""
