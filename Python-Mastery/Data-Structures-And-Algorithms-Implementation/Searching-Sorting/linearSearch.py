def linearSearch(arr, target):

	for index in range(len(arr)):
		if arr[index] == target:
			return index 
	return -1		


my_list = [7, 88, 29, 2, 6]
target = 7
print(linearSearch(my_list, target))

