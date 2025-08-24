#include <iostream>

using namespace std;

string printFriends(string name, int age, string city) {

        return name + " " + to_string(age) + " " +   city;

}





int main() {
        cout << "Function Practice" << endl;

        cout << printFriends("Manaranjan", 19, "Balarampur") << endl;
        cout << printFriends("Ujjwal", 19, "Balarampur") << endl;
        cout << printFriends("Yubraj", 21, "Baragram") << endl;

        return 0;
}




