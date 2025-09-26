# Arrays
"""
An array is a collection of elements sorted order stored in contigous memory location.

All elements of array are of same data type (int, float, etc.)

Array allow for efficient access and manipulation of data.

"""
my_list = []
my_list.append(7)
print(my_list)

import array
arr = array.array('i',[1, 2, 3, 4, 5, 6, 7])
print(type(arr), arr)



