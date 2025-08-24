#include <iostream>

using namespace std;

double cube(double n){
	return n * n * n ;
}

int main() {
	int n;
	cout << "-----Cube Calculator----- " << endl;

	cout << "Enter a number: ";
	cin >> n;

	cout << "Cube of " << n << " is: " << cube(n) << endl;

	cout << "End of the program" << endl;
		
	
	return 0;
}
