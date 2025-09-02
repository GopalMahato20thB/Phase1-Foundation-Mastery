#include <iostream>

using namespace std;

void insertionSort(int *a, int n) {

	int i,j,temp;

	for(i=1; i<n; i++) {
		temp = a[i];
		j=i-1;

		while((a[j] > temp) && (j >= 0)) {
			a[j+1] = a[j];
			j = j-1;
		} 
		a[j+1] = temp;
	}
}

void printArray(int *a, int n) {
	int i=0;
	for(i=0; i<n; i++) {
		cout << a[i] << " ";
	}
}

int main() {
	int arr[] = {2,8,1,9,4,6,0};
	int n = sizeof(arr)/sizeof(arr[0]);

	insertionSort(arr, n);
	printArray(arr, n);

	return 0;
}