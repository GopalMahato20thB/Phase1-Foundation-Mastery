
/*
my_array = [];

var i = 0;
while (i <= 5){
	my_array.push(i);
	i += 1;
}

console.log(my_array);
*/

/*
let name = "Gopal";
let name_array = [];

let i = 1;
while (i < 50){
	name_array.push(name);
	i += 1;
}

console.log(name_array.length);

*/

// Iterate with For Loops
/*
number_array = [];
for ( let i = 1; i <= 50; i++){
	number_array.push(i);
}

console.log(number_array);

// lets create a list odd numbers till 100
odd_numbers = [];
even_numbers = [];
for (let i = 1; i <= 100; i+=1){
	if (i % 2 != 0){
		odd_numbers.push(i);
	} 
	else if (i % 2 == 0) {
		even_numbers.push(i);
	}
}

console.log("Odd numbers till 100: ", odd_numbers);
console.log("Even numbers till 100: ", even_numbers);
*/


//Iterate Through an Array with a For loop
// let find out total or sum of an given array

/*
let my_array = [95, 74, 77, 85, 83]

let sum_of_values = 0;

for (let i = 0; i < my_array.length; i += 1){
	sum_of_values += my_array[i];
}

console.log("Original values: " + my_array + " Sum of this array: " + sum_of_values);

// Nesting for loops

function multiplyAll(arr){
	let product = 1;
	
	for (let i = 0; i < arr.length; i += 1){
		for (let j = 0; j < arr[i].length; j += 1){
			product *= arr[i][j];
		}
	}
	
	return product;
}

console.log(multiplyAll([[1, 2, 3], [4, 7], [9, 9]]));

// let implement this function one more time

function findProductNested(arr){
	let product = 1;

	for (let i = 0; i < arr.length; i += 1) {
		for ( let j = 0; j < arr[i].length; j += 1){
			product *= arr[i][j];
		}
	}

	return product;
}

console.log(findProductNested([[7, 7, 7], [5, 5, 5], [1, 2, 3, 4, 5, 6, 7]]))

*/

// Iterate with Do... while Loops
/*
let i = 10
my_array = []

do {
	my_array.push(i)
} while ( i < 5)

console.log(my_array)
*/

/*

let data  = [
	{
		"firstname": "Gopal Mahato",
		"contact": 6296822675,
		"email": "gopalmahatomain2026@gmail.com",
		"city": "Purulia",
		"fav_things": ["Consistent Day", "Good sleep", "Python", "Dhal Bhat"],
	},
	
	{
		"firstname": "Parayag Borakar",
		"contact": "Not Available", 
		"city": "Benarash",
		"email": "Not Available",
		"fav_things": ["Singing", "Python"]
	}	


]

function lookUpProfile(name, prop){
	for (let i = 0; i < data.length; i += 1){
		if (data[i].firstname == name){
			return data[i][prop] || "No such Property" 
		}
	}
	return "No such Data"	


}

console.log(lookUpProfile("Gopal Mahato", "email"));
console.log(lookUpProfile("Parayag Borakar", "city"));
console.log(lookUpProfile("Gopal Mahato", "city"));

*/


