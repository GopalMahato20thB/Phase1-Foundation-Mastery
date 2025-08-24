#include <iostream>

using namespace std;

//arrays in C++

int main() {

	int luckyNums[] = { 12, 7, 23, 00, 323, 99, 98 };
	cout << "Original Values: " << luckyNums << endl;
	
	cout << "Fav Num: "<< luckyNums[1] << endl;

	// modifying element i will modify the 3 number index element

	luckyNums[3] = 4000000;

	cout << "Upgraded Nums: " << luckyNums << endl;
	
	
	return 0;


}
