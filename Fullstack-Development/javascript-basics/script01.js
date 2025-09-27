console.log("My name is Gopal Mahato");
console.log("I am using Arch!");
// Data Types
// undefined, null, string, boolean, symbol, number, and object

/*
var my_name = "Sagar"
my_name = "Gopal"

let my_real_name = "Gopal Mahato"
const pi = 3.14
*/

/*
var a;
var b = 2;

a = 7;
b = a;

console.log(a)
console.log(b)
*/

// Initialize these three variables

/*
var a = 5;
var b = 10;
var c = "I am a ";



a = a + 1;
b = b + 5;
c = c + "String";
console.log("a is ", a);
console.log("b is ", b);
console.log("c is ", c);
*/

// Case Sensitivity in Variables
// Declarations

/*
var studyCapVar;
var properCamelCase;
var titleCaseOver;

// Assignments
studyCapVar = 10;
properCamelCase = "A string";
titleCaseOver = 9000;


console.log("studyCapBar is ",studyCapVar);
console.log("properCamelCase is ",properCamelCase);
console.log("titleCaseOver is",titleCaseOver);

*/
/*
// some operators two number
var sum = 10 + 10;
var subtract = 30 - 10;
var product = 8 * 8;
var divide = 10 / 5;

console.log(sum, subtract, product, divide);
*/


/*
// Increment Numbers
var myVar = 7;

myVar++;

console.log(myVar);

// Decrement Numbers
var myVar2 = 7;

myVar2--;

console.log(myVar2);
*/


/*
// decimal point number
var myDecimal = 65.4;

// multiply decimal point number
myDecimal = myDecimal * 2;
console.log(myDecimal);

// devide decimal
var quotient = 7.0 / 2;
console.log(quotient)

// finding a remainder
var remainder;
remainder = 10 % 3;
console.log(remainder, 7 % 70)  

// Compound Assignment with Augmented Addition
var a = 1;
var b = 3;
var c = 7;

console.log(a += c) // returns 8
console.log(b += a) // returns 11
console.log(c += c) // returns 14
*/

/*

//More 
var a = 5;
var s = 12;
var f = 7;

console.log(a *= 2, s *= 2, f *= 2) //returns 10, 24, 14

// another case 
var g = 1000;

console.log(g /= 10);

// declare string variable
var firstName = "Elon";
var lastName = "Musk";

console.log("Full Name: ", firstName, lastName);

// Escaping Literal Quotes in Strings
var sentences = "My name is Gopal Mahato\nI am using \"Arch Linux\" btw";
console.log(sentences);

// An alternative of this 
var sentence2 = "My nick name is 'Sagar'";
console.log(sentence2)

// We can also write this 
// another operator we can like this -= 
*/


// Concatenating Strings with Plus Operator
/*
var example_string  = "My name is Gopal Mahato" + " I am using Arch btw!";
console.log(example_string);
var new_string = " My nick name is Gopal Mahato";

example_string += new_string;

console.log(example_string);
*/

// Constructing Strings with Variables
/*
var my_name = "Gopal";
var my_nick_name = "Sagar";

var my_string = "My name Name is " + my_name + " My Nickname is " + my_nick_name;

console.log(my_string);
*/

// finding length of a string
/*
var name = "Gopal Mahato";
console.log(name.length); // for that we just use .length property
console.log(name[0]) // returns the first letter which is G

// Braket Notation to Find Nth Character in String

console.log(name[2]) // returns p

// Bracket Notation to Find Last Character in string
// To get the last element we first need to know the length then, subtract from 1 (because indexing start from 0) that way we easily find out the last element
console.log("Last element of " + name + " is ", name[(name.length) - 1]);

// Bracket Notation to Find Nth-to-Last Character in String
// second last element will be subtract by 2
console.log(name[(name.length) - 2]) // returns t like that we just find values 
*/

// Word Blanks
/*
function wordBlanks(myNoun, myAdjective, myVerb, myAdverb) {
	var result = "";
	result += "The " + myAdjective + " " + myNoun + " " + myVerb + " to the store " + myAdverb;
	return result;

}

console.log(wordBlanks("Dog", "honest","enjoy", "very"));
*/

//Store Multiple Values with Arrays
// examples
/*
var friends = ["Bimalendu", "Ujjwal", "Manaranjan"];

console.log("My friends ", friends);

var values = ["Gopal", 19.9, true];

console.log(values);

// Nested Arrays
var friends_info = [["Gopal", 19], ["Bimalendu", 19]];

console.log(friends_info);

// Access Array Data with Indexes
var home_price = [650000, 500000, 1000000]
console.log(home_price[0])  // returns the first element 650k

// Modify Array Data with Indexes
home_price[0] = 400000;
console.log("Updated home price ", home_price);
*/
// Access Muti-Dimensional Arrays with Indexes
/*
var my_array = [[1, 3, 5], [54, 5, 7], [5, 5, 5, 5, 5], [7, 12, 43, 6, 9, 0]];

console.log(my_array[0][0]); // returns 1 

// Manipulate Arrays with push()
var friends = ["Joydeep", "Soumen", "Ujjwal"];

console.log(friends);

friends.push("Manaranjan");

console.log("After adding Manaranjan ", friends);

// Manipulate Arrays with shift()


friends.shift();


console.log("After using shift() function ", friends); // shift function removes the first element
*/

// Manipulate arrays with unshift function
// So unshift function add element to the first position
/*
var my_favFoods = ["Tadka", "Rooti", "Dhal Bhat"]

console.log("Original array ", my_favFoods);

// using unshift lets add a first element 

my_favFoods.unshift("Milk")

console.log("After using unshift() function ", my_favFoods);

// An nested list example

var my_list = [["Money", 500], ["Skill", "Begginer Level"], ["Is consistency journey started", true]];

console.log(my_list);
*/

// Writing Reusable Code with Functions
/*
function ourReusableFunction(){
	console.log("Hello Wrold! I am using Arch!");
}

ourReusableFunction();
ourReusableFunction();
ourReusableFunction();
ourReusableFunction();

// Global scope and function
var name = "Sagar";

function func1() {
	return name;
}

func1();

// Local scope and function
//
function myLocalScope(){
	var myVar = 5;
	console.log(myVar);
}

myLocalScope();
// console.log(myVar); this will not work 
// Local and global variable in same program

var name_real = "Gopal";
function greet(){
	name_real = "Gopal Mahato";
	return name_real;
}

console.log(greet());

// Return a Value from a function with Return
function minusSeven(num){
	return num - 7;
}

console.log(minusSeven(10));

function multiplySeven(num){
	return num * 7;
}

console.log(multiplySeven(7));

// Understanding Undefined Value Returned from a Function
var sum= 0;
function addThree(){
	sum = sum + 3;
}

function addFive(){
	sum += 5;
}

// Assignment with a Returned Value
var changed = 0;

function change(num){
	return (num + 5) / 3;
}

changed = change(10);

var processed = 0;

function processingArg(num){
	return (num + 3) / 5;
}
processed = processingArg(7);
*/

// Stand in Line
/*
function nextInLine(arr, item){
	arr.push(item);
	return arr.shift();
}

var testArr = [1, 2, 3, 4, 5, 6 ,7];

console.log("Before: ", JSON.stringify(testArr));
console.log(nextInLine(testArr, 8));
console.log("After: ", JSON.stringify(testArr));

// boolean values
function  welcomeToBooleans(){
	return true;
}

console.log(welcomeToBooleans());

*/
// Use Conditional Logic with If statements
/*
function ourTrueOrFalse(isItTrue){
	if (isItTrue) {
		return "Yes, it is true";
	} 
	return "No it is false";
}

console.log(ourTrueOrFalse(true));
console.log(ourTrueOrFalse(false));

// Comparison with the Equality Operator
function testEqual(val) {
	if (val == 7){
		return "Equal";
	}
	return "Not Equal";
}

console.log(testEqual(7-7+7));


// Comparison with the Strict Equality Operator
console.log("--------------------------------------------")

function testStrict(val){
	if (val === 7) {
		return "Equal";
	return "Not Equal";
	}
}

console.log(testStrict(7));
//console.log(testStrict('7'));

console.log("--------------------------");

/// Compare Equality 
function compareEquality(a, b) {
	if (a == b) {
		return "Equal";
	}
	return "Not Equal";
}

console.log(compareEquality(10, "10"));
console.log(compareEquality(7, 7));

console.log("---------------------------");

function compareInEquality(a, b) {
	if (a != b) {
		return "Not Equal";
	}
	return "Equal";
}

console.log(compareInEquality(10, "10"));
console.log(compareInEquality(7, 7));
*/


//This program return given number is even or odd

/*
function evenOrOdd(num){
	return num % 2 == 0;
	
}	

console.log(evenOrOdd(7));
console.log(evenOrOdd(9));
console.log(evenOrOdd(1));
console.log(evenOrOdd(2));


// In this function we will check if number is inside or not in 10 - 20

function check(num){
	if (num <= 20 && num >= 10){
		return "Inside!";
	}
	return "Outside!";
}
console.log(check(15));
console.log(check(10));
console.log(check(20));
console.log(check(5));
console.log(check(7));

//else if and else Statements

function check_digit(num){
	if (num >= 0 && num < 10){
		return "Single Digit!";
	}
	else if (num >= 10 && num < 100){
		return "Double Digit!";
	}
	else if (num >= 100 && num < 1000){
		return "Three Digit";
	}
	else {
		return "More than three digit";
	}
}

console.log(check_digit(777));
console.log(check_digit(7));
console.log(check_digit(77));
*/

// Write chained if/else if statements to fulfill the following conditions:
// num < 5 -> "Tiny", num < 10 -> "Small", num < 15 -> "Medium", num > 20 -> "Large", num >= 20 -> "Huge"

function check_value(num){
	if (num < 0) {
		return "Tiny";
	}
	else if (num < 5) {
		return "Tiny";
	}	
	else if (num < 10) {
		return "Small";
	}
	else if (num < 15){
		return "Medium";
	}
	else if (num < 20){
		return "Large";
	}
	else if (num >= 20){
		return "Huge";
	}
}

console.log(check_value(3));
console.log(check_value(7));
console.log(check_value(13));
console.log(check_value(17));
console.log(check_value(21));
console.log(check_value(-1));


function glofScore(par, strocks){
	var names = ["Hole-in-one", "Eagle", "Birdie", "Par", "Bogey", "Double Bogey", "Go Home!"];

	if (strocks == 1){
		return names[0];
	}
	else if (strocks <= par - 2){
		return names[1];
	}else if (strocks == par - 1){
		return names[2];
	}
	else if (strocks == par){
		return names[3];
	}
	else if (strocks == par + 2){
		return names[4];
	}
	else if (strocks >= par + 3){
		return names[5];
	}
}
console.log(glofScore(5, 8));


:
