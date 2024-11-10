def linear_search(arr, target):
    """Returns the index position of the target if found, else returns -1"""

    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


arr = [2, 4, 6, 8, 10, 12]
target = 8
result = linear_search(arr, target)
print(f"Element {target} is at index: {result}")
