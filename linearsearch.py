
# Linear Search Implementation in Python
# Linear search involves checking each element in the list sequentially
# until the desired target element is found.

def linear_search(arr, target):
    # Iterate through the entire array to look for the target element
    for i in range(len(arr)):
        # If the current element matches the target, return its index
        if arr[i] == target:
            return i

    # If the target element is not found, return -1
    return -1

# Example usage:
# Given an array, find if the target element is present.
# If found, the index of the target is returned; otherwise, it returns -1.
arr = [10, 23, 45, 70, 11, 15]
target = 70
result = linear_search(arr, target)
print(f"Element {target} is at index: {result}")  # Output: Element 70 is at index: 3
