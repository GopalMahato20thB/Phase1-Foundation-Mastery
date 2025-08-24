#include <iostream>

using namespace std;

int main() {
	double num1, num2;
	char op;

	cout << "----Better version calculator----" << endl;

	cout << "Enter first number: ";
	cin >> num1;

	cout << "Enter operator(+, -, *, /): ";
	cin >> op;

	cout << "Enter second number: ";
	cin >> num2;

	if (op == '+'){
		cout << num1 + num2;
	} else if (op == '-') {
		cout << num1 - num2;
	}
	else if (op == '*'){
		cout << num1 * num2;
	} else if (op == '/') {
		if (num2 == 0) {
			cout << "Can't divisible by zero!";
		}
		else {
			cout << num1 / num2;
		}
	}
	else {
		cout << "Invalid Operator!";
	}

	cout << "\n";





	return 0;
	
	
}
