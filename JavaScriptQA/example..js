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
