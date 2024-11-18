const myName1 = "Tal.."; //define variable let = variable, const = constant

console.log(myName1); //print
let myName; // empty variable

myName = "Tal B"; // assign data to variable
console.log(`My name is: ${myName}`); //use back ticks to plug in values

console.log(typeof myName); //return type of variable

let student = {
  name: "Tal",
  age: 29,
  lastName: "Baruchi",
}; // Object - like Dict in Python

let students = ["Tal", "Koral", "Aviv"]; // Array - like List in Python

console.log(student.name);
console.log(students[1]);

let a = 1; // Global Scope

function average(a, b) {
  return (a + b) / 2;
}

console.log(`${average(5, 6)} and ${average(5, 10)}`);

// multiplication - '*'
// division - '/'
// modulus (שארית) - '%'

// assignment:
// 'value += 5' same as 'value + 5'

// comparison operations (returns bool):
// '=' assignment, '==' is equal in value, '===' is equal in value AND type
// '!=' is not equal in value, '!==' is not equal in value AND type
// '>' greater than, '<' less than, '>=' greater or equal, '<=' less or equal

// logical operators:
// '&&' - "and", true if BOTH are true
// '||' - "or", true if EITHER ONE is true
// '!Variable ===' - "not", true if variable is not equal, false if variable is equal

//incriment and decremeent:
// '++' adds 1
// '--' subtracts 1

//concatination:
// 'Value1' + ' ' + 'Value2' >>> Value1 Value2
// `${value1} and ${value2}` >>> value1 and value2

// conditional ternary operator
// let example1 = 20
// let example2 = example1 > 21 ? 'equal' : 'not equal'
// example = not equal

// functions:

// function experssions:
let dream = function () {
  console.log("My Name is Tal Baruchi");
};
console.log(typeof dream); // is of type 'function'

//loops:
//for loops:
//        start; while; step
for (let i = 1; i < 5; i++) {
    console.log(i)
  }
  //while loops:
  let counter = 1
  while(counter < 10) {
    console.log(counter)
    counter++
}

//while do loops:
// let num = 1;
// do {
//   console.log(num);
//   num += 2;
// } while (num < 20);
// // print will be 1, then increment by 2

// //infinite loops
// while(true)) {
//   console.log("lol");
// }

// array loops:
let numlist = [1, 2, 3, 4, 5, 6];
// for (let i = 0; i <= numlist.length; i++) {
//   console.log(i)
// }

//for of loops:
// for (let value of numlist){
//   console.log(value)}
// iterates over each value in the list