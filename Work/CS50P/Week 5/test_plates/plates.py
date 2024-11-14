punc = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',' ']
num = ["0","1","2","3","4","5","6","7","8","9"]
az = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

# No need for multilpe functions! just a large messy one :P

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    letters = ""
    numbers = 0
    marks = 0
    digits = ""

    for i in range(len(s)):
        if s[i] in az:
            letters += s[i]

        if s[i] in num:
            numbers += 1

        if s[i] in punc:
            marks += 1

    if marks > 0:
        return False

    if not s[0:2].isalpha():
        return False

    if numbers == 0 and marks == 0 and 2 <= len(letters) < 7:
        return True

    elif numbers > 0:
        for i in range(len(s)):
            if s[i] in num:
                digits += s[i]
        if digits and s[-len(digits):] == digits and not digits.startswith("0"):
            return True

    return False


if __name__ == "__main__":
    main()
