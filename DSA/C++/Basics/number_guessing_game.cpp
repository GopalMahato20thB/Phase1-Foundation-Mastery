#include <iostream>

using namespace std;

int main() {
	int secret_num = 7;
	int guess;
	int guess_count = 0;

	while (guess != secret_num){
		guess_count += 1;
		cout << "Enter a guess: ";
		cin >> guess;

		if (guess < secret_num){
			cout << "Too Low!" << endl;
			
		} else if (guess > secret_num){
			cout << "Too High!" << endl;
		}
		
	}
	cout << "Its perfect guess!\nTotal number of guesses: " << guess_count << endl;

	return 0;
	
}
