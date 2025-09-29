//Swap two numbers without using a third variable

function swapNumber(a, b){
	a = a + b 
	b = a - b 
	a = a - b 
	
	return [a, b]
}

console.log(swapNumber(7, 9))
console.log(swapNumber(100, 95))



