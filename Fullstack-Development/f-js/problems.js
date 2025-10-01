/*
Problem 1: Basic Declaration Differences
Declare three variables x, y, and z using var, let, and const respectively, 
all initialized to 5. Then, reassign x = 10 and y = 10. 
What are the final values of each, and why can't you reassign z?
*/
// I declare three values like this 
var x = 5;  // this  is the old way of declaring variables in Javascript. Variables declared with var can be reassigned and redeclared.
let y = 5;  // this is the modern way of declaring block-scoped variables. Variables declared with let can also be reassigned, but can not be redeclared in the same scope.
const z = 5; // this const means We can't reassigned it after initialization. 

// Now let's reassign according to the problem 

x = 10;
y = 10;
// z = 7;

/*
// Problem 

var a;  // hoisted, initialized as undefined
console.log(a); // prints undefied 
var a = 3; // now a is assigned to 3

console.log(b); // this will give me reference error
*/

// problem 3
if (true) {
  var c = 3;
  let d = 4;
}
//console.log(c); // it will return value of c
//console.log(d); // it will throws an error 



