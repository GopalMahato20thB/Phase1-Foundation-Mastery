# Bubble sort implementation
def bubble_sort(arr):
	for passes in range(len(arr)):
		for i in range(len(arr) - 1 - passes):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]

	return arr 


unsorted_array = [2, 4, 7, 1, 3, 67, 20]
print(bubble_sort(unsorted_array))