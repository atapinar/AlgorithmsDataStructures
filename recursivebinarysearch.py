def recursive_binarysearch(arr, target):
    if len(arr) == 0:
        return False
    else:
        midpoint = len(arr) // 2

        if arr[midpoint] == target:
            return True
        else:
            if arr[midpoint] < target:
                # Search in the right half
                return recursive_binarysearch(arr[midpoint+1:], target)
            else:
                # Search in the left half
                return recursive_binarysearch(arr[:midpoint], target)

def verify(result):
    if result:
        print("Target found:", result)
    else:
        print("Target not found:", result)

# Testing the code
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
result = recursive_binarysearch(numbers, 12)
verify(result)

result = recursive_binarysearch(numbers, 7)
verify(result)
