//1
let numArray = [2, 4, 6, 7, 8, 12, 64, 631];

for (let i = 0; i <= numArray.length; i++) {
  //Iterate over indices, go past 7
  try {
    if (numArray[i] !== undefined) {
      console.log(numArray[i]); // Iterate over Array and print each element
    } else if (numArray[i] === undefined) {
      throw new Error("Out of bounds"); // Throw error if element is undefined
    }
  } catch (error) {
    console.log("Error:", error.message); //Catch thrown error
  }
}

//2
let person = { firstName: "Peter", lastName: "Parker", city: "New York" };

function objectPrint(a, b) {
  if (a[b] !== undefined) {
    console.log(a[b]); // Print value of given object[key]
  }
  try {
    if (a[b] === undefined) {
      throw new Error("No such key"); // Throw error if undefined
    }
  } catch (error) {
    console.log("Error:", error.message); //Catch thrown error
  }
}
try {
  objectPrint(person, "firstName");
  objectPrint(person, "blol");
  objectPrint(pen, "blol");

  
} catch (error) {
  console.log("Error: No such object"); //Immediately catch ReferenceError of object
}
