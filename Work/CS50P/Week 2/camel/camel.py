
name = input("camelCase: ")
snake_case = ""

for c in name:
    if c.isupper():
        snake_case += "_"
        snake_case += c

    else:
        snake_case += c

snake_case = snake_case.casefold()

print(snake_case)









