#include <iostream>

using namespace std;

double get_max(int num1, int num2, int num3){
	double result;

	if (num1 >= num2 && num1 >= num3){
		result = num1;
	}
	else if (num2 >= num1 && num2 >= num3){
		result = num2;
	}
	else {
		result = num3;
	} 

	

	return result;
}


int main() {

	int num1, num2, num3;

	cout << "----Finding Max between 3 numbers----" << endl;

	cout << "Enter first number: ";
	cin >> num1;
	cout << "Enter second number: ";
	cin >> num2;
	cout << "Enter third number: ";
	cin >> num3;

	cout << "Max number is: " << get_max(num1, num2, num3) << endl;

	cout << "\nButtom of the program\n";
	return 0;
}
