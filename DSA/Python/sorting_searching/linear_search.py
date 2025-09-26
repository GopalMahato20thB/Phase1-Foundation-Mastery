# Linear Search
# return the target index if present else -1

def linear_search(arr, target):

    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [4, 2, 7, 0, 24, 9]
print(linear_search(my_list, 7))
