//Functions:

//1.
const multiply = (a, b) => a * b;
console.log(multiply(5, 20));

//2.
const add = (a, b) => a + b;
console.log(add(20, 20));

//3.
const greet = (name) => `Welcome, ${name}`;
console.log(greet("Tal"));

//4.
const convert = (C) => `${(C * 9) / 5 + 32}F`;
console.log(convert(24));

//5.
let person1 = {
  firstName: "Tony",
  lastName: "Soprano",
  age: 45,
  memebership: true,
};

let person2 = {
  firstName: "Keanu",
  lastName: "Reeves",
  age: 16,
  membership: true,
};

function isElligable(object) {
  return `${object.firstName} is ${
    object.memebership && object.age > 18 ? "elligable" : "not elligable"
  }`;
}

console.log(isElligable(person1));
console.log(isElligable(person2));


for (let key in person1) {
    console.log(person1[key])
}