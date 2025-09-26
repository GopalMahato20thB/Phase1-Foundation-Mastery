# Bubble sort algorithm

def bubble_sort(arr):

    for index in range(len(arr)):
        if arr[index + 1] > arr[index]:
            arr[index], arr[index + 1] = arr[index + 1], arr[index]













unsorted_list = [12, 7, 6, 23, 9, 90]
print(bubble_sort(unsorted_list))
