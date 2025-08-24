#include <iostream>

using namespace std;

int getMax(int num1, int num2){
	int result;

	if (num1 > num2) {
		result = num1;
	} else {
		result = num2;
	}
	return result;
}


int main() {

	int num1, num2;

	cout << "-----Max between two number program-----" << endl;
	
	cout << "Enter first number: ";
	cin >> num1;

	cout << "Enter second number: ";
	cin >> num2;

	cout << "Max number is: " << getMax(num1, num2) << endl;

	cout << "Button of the program!" << endl;
	

	return 0;
}
