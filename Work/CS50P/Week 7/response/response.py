from validator_collection import checkers

if checkers.is_email(input("Your email adress: ").lower()):
    print("Valid")
else:
    print("Invalid")






