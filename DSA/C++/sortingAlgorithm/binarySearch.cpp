#include <iostream>

using namespace std;

int binarySearch(int *a, int n, int target ) {
	int s=0, e=n-1;
	int mid = (s+e)/2;

	while(s<=e && a[mid] != target) {
		if(a[mid]<target){
			s = mid+1;
		} else{
			e = mid-1;
		}

		mid = (s+e)/2;
	
   }
	if(s>e) {
		return -1;
	} else {
		return mid;
	}

 
	
}

void printArray(int a[], int n) {
	for(int i=0; i<n; i++) {
		cout << a[i] << " ";
	}
}


int main() {
	int arr[] = {2,4,6,8,9,20};

	int size = sizeof(arr)/sizeof(arr[0]);
	printArray(arr, size);
	cout << endl;

	int target;
	cout << "Enter a number: ";
	cin >> target;

	int result = binarySearch(arr, size, target);

	if(result == -1) {
		cout << "target not found" << endl;
	} else {
		cout << "target found in index " << result << endl;
	}
	return 0;
}
