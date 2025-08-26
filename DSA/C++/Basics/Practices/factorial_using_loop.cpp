#include <iostream>
using namespace std;
/*
Factorial of a number
Input: N
Output: N! = N × (N-1) × ... × 1.
*/

int main() {
    int factorial = 1, n;
    cout << "Enter N: ";
    cin >> n;
    
    
    for (int i = n; i > 0; i--){
        factorial *= i;
    
    }

    cout << "Factorial of " << n << " is: " << factorial << endl;
    return 0;
}