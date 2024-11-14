answer = (input("What is the Answer to the Great Question of Life, the Universe and Everything? ").lower().strip())

match answer:
    case "forty-two" | "forty two" | "42":
        print("Yes")

    case _:
        print("No")
