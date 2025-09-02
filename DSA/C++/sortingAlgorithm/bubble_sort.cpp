#include <iostream>

using namespace std;


void bubbleSort(int *a, int n) {
	int temp,i;
	for( i=0; i<n; i++){
		for(int j=0; j < n-i; j++) {
			if(a[j] > a[j+1]) {
				temp = a[j];
				a[j] = a[j+1];
				a[j+1] = temp;
			}				
		}
	}
}



int main() {
	int a[] = {3,4,5,3,1,8,0,8};
	int n = sizeof(a)/sizeof(a[0]);

	bubbleSort(a,n);

	for(int i=0; i<n; i++) {
		cout << a[i] << " ";
	}
	// std::cout << "coder" << std::endl;
	return 0;
}