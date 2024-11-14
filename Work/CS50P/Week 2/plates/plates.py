punc = ['!', '"', '#', '$', '%', '&', "'", '(', ')',
 '*', '+', ',', '-', '.', '/', ':', ';', '<',
  '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',' ']

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    if length(s) and marks(s) and letters(s) and digits(s):
        return True

def length(s):
    if 2 <= len(s) < 7:
        return True

def marks(s):
    for i in s:
        return False if i in punc else True

def letters(s):
    return True if s[:2].isalpha() else False

def digits(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True if s[i:].isdigit() and s[i] != "0" else False
    return True
    




if __name__ == "__main__":
    main()
    

#  elif numbers > 0:
 #       for i in range(len(s)):
  #          if s[i].isdigit():

#                for j in s[i+1:]:
#                   if j.isdigit():
#                       return True