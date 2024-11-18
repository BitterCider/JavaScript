//1 
function isCount(a){
for (let i = 1; i <= 10; i++){
    if (i === a && a % 2 === 0){
        console.log('ERROR');
        continue;
    }
    console.log(i)
    }
}

isCount(4)
isCount(7)

//2 while:
let num = 20
while(num > 0){
    console.log(num)
    num--
}

//2 while-do:
do{
    console.log(num)
    num--
} while(num > 0)


//3
let arrExample = ['Mango', 'Juice', 'Mouse', 'Hornet', 'Picture', 'Chinese']

for (element of arrExample){
    console.log(element)
}

//4
let objExample = {occupation: 'Spy',
    lastName: 'Bond',
    firstName: 'James',
    alias: '007'
}

objExample.occupation = 'Accountant'

for (key in objExample){
    console.log(objExample[key])
}