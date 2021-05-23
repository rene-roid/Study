// In JavaScript there are 3 types to declare variables var, let and const
// Variables are made to store data in a keyword

// Variable Var
var myName = 'Yuuki';
console.log(myName);

// var is used to declare a new variable
// myName is the name tha i gave to my variable
// = it assigns the value to the varible
// 'Yuuki' is the value of the variable myName


// Variable let
// Let is a varible that can be reasigned (edited) and it can start with no value.

let money = 2000;
console.log(money);
money = 1000;
console.log(money);

// 
let friends; // let starting with no value
console.log(friends); // Prints undefined
friends = '0 friends';

console.log('Lol ' + myName + ' has ' + friends);


// Variable const
// Const is a variable that it is constant, it is the same as var or let but it cannot be edited or changed
const chocolate = 'expensive';
console.log('Chocolate is ' + chocolate)