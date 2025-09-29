/*
Find the largest number in an array
Find the smallest number in an array
Remove duplicates from an array
Flatten a nested array (`[1, [2, [3]]]` → `[1,2,3]`)
Rotate an array by k steps
Implement map manually
Implement filter manually
Implement reduce manually
*/

function largestNumber(arr){

	if (!Array.isArray(arr) || arr.length === 0){
		return null;
	}




	let max = arr[0];
	for (let i = 0; i < arr.length; i += 1){
		if (typeof arr[i] === "number" && arr[i] > max){
			max = arr[i];
		}
	}
	return max;
}

console.log(largestNumber([1, 3, 4, 3, 0, 7]));

// finding the smallest number in an array

function smallestNumber(arr){
	if (!Array.isArray(arr) || arr.length === 0){
		return null;
	}
	
	min = arr[0];
	for (let i = 0; i < arr.length; i += 1){
		if (typeof arr[i] === "number" && arr[i] < min){
			min = arr[i];
		}
	}
	return min;

}

console.log(smallestNumber([1, 3, 4, 3, 0, 7]));

// Removing duplicates from an array

function removeDuplicates(arr){
	let uniques = [];
	let seen = {};

	for (let i = 0; i < arr.length; i += 1){
		if (!seen[arr[i]]){
			seen[arr[i]] = true;
			uniques.push(arr[i]);
		}
	}
	return uniques;
}

console.log(removeDuplicates([1, 1, 1, 2, 2]));

// very short approch
 function rD(arr){
	 return [...new Set(arr)];
}

console.log(rD([1, 2, 2, 2, 7]));
