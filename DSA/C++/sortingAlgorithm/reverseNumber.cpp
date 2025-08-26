#include <iostream>

using namespace std;

int reverseNum(int n) {
	int rev= 0, digit;

	while(n>0){
		digit = n%10;  // reminder
		rev = rev*10 + digit; // store reminder
		n= n/10; // qoutient or removing the last digit
	}

	return rev;
}

int main() {
	int n;

	cout << "Enter a number: ";
	cin >> n;

	int result = reverseNum(n);
	cout << result<< endl;
	return 0;
}
