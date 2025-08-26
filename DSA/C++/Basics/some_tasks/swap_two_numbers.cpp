// Write a program to swap two numbers (without using temp variable).

#include <iostream>
#include <cmath>

int main(){
	int m, n, temp;
	std:: cout << "Enter first number: ";
	std:: cin >> m ;
	std:: cout << "Enter second number: ";
	std:: cin >> n;

	std:: cout << m << " " << n << std:: endl; 

	temp = m;
	m  = n;
	n = temp;

	std:: cout << m << " " << n << std:: endl;
	
	

	std:: cout << "Hello Arch!" << std:: endl;
	return 0;
}

