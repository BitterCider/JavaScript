// //1
// function numtype(a) {
//   if (a > 0) {
//     console.log(a, "is positive");
//   } else if (a < 0) {
//     console.log(a, "is negative");
//   } else {
//     console.log("a is zero");
//   }
// }

// numtype(5);
// numtype(-6);
// numtype(0);

// //2
// let person = {firstName:'Bruce',
//     lastName:'Wayyne',
//     Age:'35'
// }

// let isAdult = (age => 18) ? 'Adult':'Minor'
// console.log(isAdult)

//3
let student1 = { firstName: "Susy", lastName: "Bale", class: "A1", grade: 70 };

let student2 = {
  firstName: "Roxana",
  lastName: "Wright",
  className: "A1",
  score: 56,
};

let student3 = { firstName: "Mel", lastName: "Borne", class: "A1", grade: 89 };

let student4 = {
  firstName: "Mildred",
  lastName: "Cohurt",
  className: "A1",
  score: 90,
};

let student5 = {
  firstName: "Milenoe",
  lastName: "Snow",
  className: "A1",
  score: 79,
};

function grade(student) {
  switch (true) {
    case student.score >= 90:
      console.log(student, "grade: A");
    break;
    case student.score >= 80:
      console.log(student, "grade: B");
    break;
    case student.score >= 70:
      console.log(student, "grade: C");
    break;
    case student.score >= 60:
      console.log(student, "grade: D");
    break;
    case student.score < 60:
      console.log(student, "grade: F");
  }
}

grade(student2)
grade(student4)

//4
function leapYear(year){
    if (year % 4 === 0 && year % 100 != 0 || year % 400 === 0){
        console.log(year, 'is a leap year')
    } else{
        console.log(year ,'is not a leap year')
    }}


leapYear(2000)
leapYear(2011)

