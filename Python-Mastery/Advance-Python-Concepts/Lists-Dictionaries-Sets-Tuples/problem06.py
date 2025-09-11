#Rotate list k position
# input [1, 2, 3, 4, 5] output: [4, 5, 1, 2, 3]
def reverse_array(start, end, arr):

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start, end = start + 1, end - 1

    return arr

def rotate_array(arr, k):
    n = len(arr)
    k = k % n

    reverse_array(0, n - 1, arr)
    reverse_array(0, k - 1, arr)
    reverse_array(k, n - 1, arr)

    return arr
nums = [1, 2, 3, 4, 5]
print(rotate_array(nums, 2))
