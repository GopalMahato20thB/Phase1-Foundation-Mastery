
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





