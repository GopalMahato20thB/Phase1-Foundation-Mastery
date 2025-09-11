#Level Beginner
# 1. Create a list of 10 numbers. Print the maximum, minimum, and average.

def getMaxMinAvg():
    arr = []
    for i in range(10):
        element = int(input("Enter a number: "))
        arr.append(element)
    return f"Max: {max(arr)} | Min: {min(arr)} | Average: {sum(arr) / len(arr)}"

print(getMaxMinAvg())

