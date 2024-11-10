def recursive_binary_search(list, target, start=0, end=None):
    if end is None:
        end = len(list) - 1
    if start > end:
        return -1

    mid = (start + end) // 2

    if target == list[mid]:
        return mid
    else:
        if target < list[mid]:
            return recursive_binary_search(list, target, start, mid-1)
        else:
            return recursive_binary_search(list, target, mid+1, end)



arr = [2, 4, 6, 8, 10, 12]
target = 8
result = recursive_binary_search(arr, 0, len(arr) - 1, target)
print(f"Element {target} is at index: {result}")
