def binary_search(arr, target):
    first = 0
    last = len(arr) - 1

    while first <= last:
        midpoint = (first + last)//2
        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint+1
        else:
            last = midpoint-1
    return -1


arr = [10, 23, 45, 70, 11, 15]
target = 5
result = binary_search(arr, target)
print(f"Element {target} is at index: {result}")
