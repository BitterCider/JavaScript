Expression = input("Expression: ")
x, y, z = Expression.split(" ")
num1 = int(x)
num2 = int(z)


match y:
    case "+":
        result = num1 + num1
        print(float(result))

    case "-":
        result = num1 - num2
        print(float(result))

    case "/":
        result = (num1 / num2)
        print(float(result))

    case "*":
        result = (num1 * num2)
        print(float(result))


