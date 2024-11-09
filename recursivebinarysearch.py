
# Recursive Binary Search Implementation in Python
# Similar to the iterative version, binary search recursively splits the sorted array
# to find the target value.

def recursive_binary_search(arr, low, high, target):
    # Base case: if the low index exceeds the high, the target is not in the array
    if low > high:
        return -1

    # Calculate the middle index of the current search range
    mid = (low + high) // 2

    # If the middle element matches the target, return its index
    if arr[mid] == target:
        return mid
    # If the middle element is smaller than the target, search in the right half
    elif arr[mid] < target:
        return recursive_binary_search(arr, mid + 1, high, target)
    # If the middle element is larger than the target, search in the left half
    else:
        return recursive_binary_search(arr, low, mid - 1, target)

# Example usage:
# Recursive search within a sorted array to locate the target element.
# If found, the index of the target is returned; otherwise, it returns -1.
arr = [2, 4, 6, 8, 10, 12]
target = 8
result = recursive_binary_search(arr, 0, len(arr) - 1, target)
print(f"Element {target} is at index: {result}")  # Output: Element 8 is at index: 3
