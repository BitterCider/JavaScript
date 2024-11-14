
filename = (input("File name: ").casefold().strip())

type = filename.split(".")[-1]

match type:
    case "jpeg" | "gif" | "png":
        print("image/" + type)

    case "jpg":
        print("image/jpeg")

    case "txt":
        print("text/plain")

    case "pdf":
        print("application/" + type)

    case "zip":
        print("application/" + type)

    case _:
        print("application/octet-stream")

















