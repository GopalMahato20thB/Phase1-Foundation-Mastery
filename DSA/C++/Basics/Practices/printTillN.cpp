#include <iostream>

using namespace std;

/* 
1. Print numbers from 1 to N
Input: N
Output: Numbers from 1 to N on the same line.
*/



int main() {
    int n;
    cout << "Enter N: ";
    cin >> n;
    
    for (int i = 1; i <= n; i++){
        cout << i << endl;
    
    }    
    
    
    return 0;
}