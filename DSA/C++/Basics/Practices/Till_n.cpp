#include <iostream>
using namespace std;
/*
Sum of first N natural numbers
Input: N
Output: Sum = 1 + 2 + 3 + ... + N.
*/

int main() {
    int n, sum_of = 0;
    cout << "Enter N: ";
    cin >> n;
    
    for (int i = 0; i <= n; i++) {
        sum_of += i;
        
    }
    cout << "Sum of number till N: " << sum_of << endl;

    
    return 0;
}