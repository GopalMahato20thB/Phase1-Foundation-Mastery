#include <iostream>
using namespace std;
/*
Reverse counting
Input: N
Output: Print numbers from N down to 1.
*/

int main() {
    int n;
    cout << "Enter N: ";
    cin >> n;
    
    for (int i = n; i > 0; i--){
        cout << i << " ";
    
    }
    
    return 0;
}