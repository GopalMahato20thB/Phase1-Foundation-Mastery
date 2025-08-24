#include <iostream>

using namespace std;

int main() {
	// taking integers 
	int age;
	string name;

	cout << "Enter Your Name: ";
	getline(cin, name);

	cout << "Enter Your age: ";
	cin >> age;

	cout << "Hello " << name << " You are " << age << " years old\nYou are in Your PRIME!" << endl;
	
	
	return 0;
}
