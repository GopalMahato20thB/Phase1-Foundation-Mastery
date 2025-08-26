#include <iostream>
#include <cmath>

using namespace std;

int main() {
	int n;
	cout << "Enter N: ";
	cin >> n;

	if (n <= 1){
		cout << "Not prime!" << endl;
		return 0;
	}

	bool is_prime = true;

	for (int i = 2; i <= sqrt(n); i++){
		if (n % i == 0){
			is_prime = false;
			break;
		}
	}


	if (is_prime){
		cout << "Prime Number!" << endl;
		
	} else {
		cout << "Not Prime!" << endl;
	}

	return 0;
}
