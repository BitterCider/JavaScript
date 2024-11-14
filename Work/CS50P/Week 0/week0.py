# ***notes***

# assignment function "=" - from right to left
# str - "string"
# int - whole numbers
# paramaters e.g - "end=" ends the line. "sep=" - seperates the previous 2 arguments.

#name = input ("What's your name? ")

# remove whitespace from str and capitalize name in 1 function
#name = name.strip().title()

# capitalize name
# name = name.title()

# split name into first and last name
#first, last = name.split(" ")


#print (f"hello, {first}")


# def - creating, defining new functions

#mine
"""
def hello():
    print(f"hello, {name}")

name = input("What's your name? ")
hello()
"""

#lesson
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("hello,", to)

main()









