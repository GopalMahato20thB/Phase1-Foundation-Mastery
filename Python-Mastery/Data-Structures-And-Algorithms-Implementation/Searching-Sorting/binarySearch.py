"""
1. I will consider the full arraylist. start is 0 end len(arr - 1)
2. See the middle element. middle = end + start // 2
3. We compare element at middle with target.  

"""

def binarySearch(arr, target):
	start = 0
	end = len(arr) - 1

	while start <= end:
		mid = (start + end) // 2

		if arr[mid] == target:
			return mid
		elif arr[mid] > target:
			end = mid - 1
		else:
			start = mid + 1		
	return -1		

sorted_list = [2, 4 , 6, 7, 99, 123]
target = 7
print(binarySearch(sorted_list, target))