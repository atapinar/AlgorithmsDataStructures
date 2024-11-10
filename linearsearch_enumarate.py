def linear_search(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1


arr = [10, 23, 45, 70, 11, 15]
target = 45
result = linear_search(arr, target)
print(f"Element {target} is at index: {result}")