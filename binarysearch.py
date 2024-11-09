
# Binary Search Implementation in Python
# Binary search works on sorted arrays. The idea is to divide the array into halves
# and compare the middle element with the target value to find the target efficiently.

def binary_search(arr, target):
    # Set initial pointers for the beginning (low) and end (high) of the array
    low = 0
    high = len(arr) - 1

    # Continue searching while there is a valid portion of the array
    while low <= high:
        # Calculate the middle index of the current search range
        mid = (low + high) // 2
        
        # If the middle element is equal to the target, return its index
        if arr[mid] == target:
            return mid
        # If the middle element is smaller than the target, adjust the search range to the right half
        elif arr[mid] < target:
            low = mid + 1
        # If the middle element is larger than the target, adjust the search range to the left half
        else:
            high = mid - 1

    # If the target element is not found, return -1
    return -1

# Example usage:
# Given a sorted array, find if the target element is present.
# If found, the index of the target is returned; otherwise, it returns -1.
arr = [1, 3, 5, 7, 9, 11]
target = 5
result = binary_search(arr, target)
print(f"Element {target} is at index: {result}")  # Output: Element 5 is at index: 2
