# Level Beginner
# Reverse a list without using the reverse method.

def reverse_list(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

print(reverse_list([1, 3, 7, 5, 99]))
