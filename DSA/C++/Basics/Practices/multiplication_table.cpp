#include <iostream>
using namespace std;
/*
Multiplication table
Input: N
Output: Print multiplication table of N up to 10.
*/

int main() {
    int n;
    cout << "Enter a Number: ";
    cin >> n;
    
    for (int i = 1; i <= 10; i++) {
        cout << n << " x " << i  << " = " << n*i << endl;
    
    }

    
    return 0;
}