# Quicksort - Recursive Implementation
# Divide and Conquer algorithm
# Picks an element as a pivot and partitions array around pivot

# Possible choices for pivot
# 1. Always pick first element
# 2. Always pick last element
# 3. Pick random element
# 4. Pick median element (middle index)

# Time complexity
# Worst-Case O(n^2) - array sorted in reverse order
# Best-Case O(nlogn)

# Advantages over MergeSort
# In-place so does not require extra storage
# Though both are O(nlogn) average time complexity,
# Quicksort has a faster constant factor due to operations in place


from random import randint


# Implementation below takes last element as pivot


def partition(arr: list, low: int, high: int) -> None:
    # Low always marks the lowest unset index in the partition
    # We will repeatedly swap numbers < pivot with low index
    # Take pivot to be last/high index in this implementation
    pivot = arr[high]
    for j in range(low, high):
        # If item <= pivot, swap places with index i and increase i
        if arr[j] < pivot:
            arr[low], arr[j] = arr[j], arr[low]
            low += 1

    # After loop, all items smaller than pivot are placed before index i
    # We swap i and pivot so that pivot is in the right place
    # All items after pivot must be larger than pivot
    arr[low], arr[high] = arr[high], arr[low]
    # Return index of pivot
    return low


# Main quicksort function
# Sort in place so no return value
def quickSort(arr: list, low, high) -> None:
    # Base cases - single element array or if partition is one element in length
    if len(arr) == 1 or high <= low:
        return None

    # First pass will partition entire array and return location of pivot
    idx = partition(arr, low, high)

    # Recursively sort numbers less than partition and numbers greater than partition
    # arr[idx] = previous pivot, so already in the right place
    quickSort(arr, low, idx - 1)
    quickSort(arr, idx + 1, high)


# Example 1
arr = [10, 7, 8, 9, 1, 5]
print("Array:", arr)
quickSort(arr, 0, len(arr) - 1)
print("Sorted:", arr)
print()

# Example 2
arr = [5, 4, 8, 8, 8, 3, 10, 1, 21]
print("Array:", arr)
quickSort(arr, 0, len(arr) - 1)
print("Sorted:", arr)
print()
