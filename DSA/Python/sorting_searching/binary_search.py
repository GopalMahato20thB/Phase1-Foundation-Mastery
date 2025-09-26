
def binary_search(arr, target):
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

    
arr = [13, 45, 67, 99, 100, 998]
target = 99

print(binary_search(arr, target))

