groceries = {}
while True:
        try:
            item = (input(""))
            if item in groceries:
                groceries[item] += 1
            else:
                groceries[item] = 1
        except EOFError:
           sort_groceries = dict(sorted(groceries.items()))
           for i in sort_groceries:
                print(sort_groceries[i], i.upper())
           break

























