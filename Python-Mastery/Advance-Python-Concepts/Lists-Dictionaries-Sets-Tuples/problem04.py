# Level Intermidiate
# Write a program to find the second largest number in a list.

def second_largest(arr):
    if len(arr) < 2:
        return "List must have at least two elements."
    else:
        max_element = float("-inf")
        second_element = float("-inf")

        for i in arr:
            if i > max_element:
                second_element = max_element
                max_element = i
            elif max_element > second_element and i != max_element:
                second_element = i
        if second_element == float("-inf"):
            return "No distinct second element found (e.g., all elements are the same)"
        else:
            return f"Second Largerst (iterative): {second_element}"
print(second_largest([1, 2, 3, 4, 5, 6, 7]))
