cent = 50
print(f"Amount Due: {cent}")

while 0 < cent <= 50:
    pay = int(input("Insert Coin: "))

    if pay != 25 and pay != 10 and pay != 5:
        print(f"Amount Due: {cent}")

    else:
        cent = cent - pay
        if cent > 0:
            print(f"Amount Due: {cent}")

        if cent <= 0:
           print(f"Change Owed: {abs(cent)}")
           break































