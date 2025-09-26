#include <iostream.h>

using namespace std;

void selectionSort(int *a, int n) {

	int i,j
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

	selectionSort(arr, n);
	printArray(arr, n);
	return 0;
}