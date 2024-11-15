// Objects

//1.
let Person = {
    firstName: 'Adam',
    lastName: 'Levy',
    age: 26,
    occupation: 'QA engineer',
    education: '15 years' 
}

console.log(Person)

//2.
Person.hobbies = 'Skiing, Cooking'
Person.height = '1.83 cm'

console.table(Person)

//3.
Person.age = 29
Person.hobbies = 'Cooking, Guitar'

console.table(Person)