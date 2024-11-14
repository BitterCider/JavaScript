#while - calling a loop
#for - calling a loop
#list [] - another type of data, contains multiple values in the same variable
#range ()
#len - returns the length of a list as int
#dict {}- dictionaries, allows to associate one value to another

               #key         #value
#students = {"Hermione": "Gryffindor", #and so on}

#when using a loop 'for' with a dictionary, the loop iterates over the keys, not the values.
#eg of dictionaries within a list:
"""
students = [{"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
             {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
             {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell"},
             {"name": "Draco", "house": "Slytherin", "patronus": None }]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
         # student is dictionary on list, [] is key, prints value
"""

# nested loops - c


