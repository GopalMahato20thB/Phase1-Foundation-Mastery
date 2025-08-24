#include <iostream>

using namespace std;

int main() {
	bool isMale = false;
	bool isTall = true;

	if (isMale == true && isTall == true){
		cout << "You are tall  Men" << endl;
	} 

	else if(isMale == true && !isTall){
		cout << "You are short man!" << endl;
	}

	else if (isMale == false && isTall) {
		cout << "You are tall but not male" << endl;
	}
	
	else {
		cout << "You are not tall  and not men" << endl;
	}
	

	return 0;
}
