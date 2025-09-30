//Count vowels in a string


function countVowels(s){
	let vowels = ["a", "e", "i", "o", "u"]
	let count_vowels = 0
	for (let i = 0; i < s.length; i++){
		if (vowels.includes(s[i].toLowerCase())) {
			count_vowels += 1
		}
	}
	return count_vowels		
}

console.log(countVowels("Gopal"))
console.log(countVowels("AEIOU")) // returns 5
console.log(countVowels("Javascript")) // returns 3



// Find the longest word in a sentence

// Reverse a string manually

function reverseString(s){
	let reverse_string = ""

	for (let i = s.length - 1; i >= 0; i -= 1){
		reverse_string += s[i]
	}
	return	reverse_string
}

console.log(reverseString("Gopal"))
 
//check if a string is a palindrome

function isPalindrome(s){
	s = s.toLowerCase()
	return s === reverseString(s)
}


console.log(isPalindrome("Gopal"))
console.log(isPalindrome("Madam"))


// Manual Palindrome Check 
console.log("----- This function is called isPalindrome -----");

function isPalindromeManual(s){
	s = s.toLowerCase();
	
	let left = 0;
	let right = s.length - 1;

	while (left < right){
		if (s[left] !== s[right]){
			return false;
		}
		left +=1 ;
		right -= 1;
	}
	return true;
}

console.log(isPalindromeManual("Gopal"));
console.log(isPalindromeManual("Mam"));

console.log("--------------------------------------------");
//Find the longest word in a sentence

function longestWord(sentence){
	max = 0;
	current_max = 0;

	for (let i = 0; i < sentence.length; i += 1){
		if (sentence[i] != " "){
			current_max += 1;
		}else {
			if (current_max > max){
				max = current_max;
			}
			current_max = 0;
		}
		
	} 
	if (current_max > max){
		max = current_max;
	}

	return max;
}

console.log(longestWord("My name is Gopal Mahato"));
console.log(longestWord("She is very beautifull"));
console.log(longestWord("She is Happy girl"));

