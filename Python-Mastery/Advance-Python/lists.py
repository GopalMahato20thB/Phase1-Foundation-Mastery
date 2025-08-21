my_list = ["banana", "cherry", "Mango", "Guava"]

# checking total items by using len built-in function

print("Total Items: ", len(my_list))

# removing the last element by using pop

print("The last element is: ", my_list.pop())

## reversing the list

def reverse_array(arr):
    start, end = 0, len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[end]
        start += 1
        end -= 1

    return arr
print("Original: ", my_list)
print("Reverse Form: ")
print(reverse_array(my_list))

