#include <iostream>
using namespace std;
/*
Even numbers in a range
Input: N
Output: Print all even numbers from 1 to N.
*/

int main() {
    int n;
    cout << "Enter N: ";
    cin >> n;
    
    for (int i = 1; i <= n; i++){
    
        if (i % 2 == 0) {
            cout << i << " ";
            
        
        }
    }
    
    
    return 0;
}