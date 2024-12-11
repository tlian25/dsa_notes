# Merge Sort
# Divide and Conquer algorithm
# Divides input array into two halves
# Recursively calls itself on each half
# Then merges two halves together in sorted order

# Psuedo Code
# 1. Find middle point to divide array in half
# 2. Call mergeSort for first half
# 3. Call mergeSort for second half
# 4. Merge two halves together


# Recursive Solution
def mergeSort(arr: list) -> list:
    # Base case
    if len(arr) <= 1:
        return None

    # Instantiate a copy of left half and right half of the array
    mid = len(arr) // 2
    Larr = arr[:mid]  # left half
    Rarr = arr[mid:]  # right half

    # Recursively sort halves
    mergeSort(Larr)
    mergeSort(Rarr)

    # Set last element to INF as a stopping point
    # Make sure we stop one element short of INF
    Larr.append(float("inf"))
    Rarr.append(float("inf"))

    # Merge Together
    i = 0  # idx for Larr
    j = 0  # idx fof Rarr
    k = 0  # idx for merged array, will set arr in place
    while i < len(Larr) - 1 or j < len(Rarr) - 1:
        if Larr[i] < Rarr[j]:
            arr[k] = Larr[i]
            i += 1
        else:
            arr[k] = Rarr[j]
            j += 1
        k += 1

    # At end, i == len(Larr)-1 => Larr[i] == INF and same for j


print("Merge Sort - Recursive\n")

# Example 1
arr = [10, 7, 8, 9, 1, 5]
print("Array:", arr)
mergeSort(arr)
print("Sorted:", arr)
print()

# Example 2
arr = [5, 4, 8, 8, 8, 3, 10, 1, 21]
print("Array:", arr)
mergeSort(arr)
print("Sorted:", arr)
print()

# Example 3
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Array:", arr)
mergeSort(arr)
print("Sorted:", arr)
print()
