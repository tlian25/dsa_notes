# K-th Largest Element
# More efficient method to pull k-th largest element from an array
# Sorting will take O(nlogn) time complexity
# We can use same logic as quicksort, but stopping when we've found the pivot == k
# We only ever need to consider half the array
# Time complexity = n + n/2 + n/4 + n/8 ... on average = O(2n)

# Same partition function as quicksort

# Return index where Pivot is placed at the end of swapping
# Partitioning just means:
# elements left of pivot are < pivot, not necessarily sorted
# elements right of pivot are >= pivot, not necessarily sorted
def partition(arr:list, low:int, high:int) -> int:
    
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[low], arr[j] = arr[j], arr[low]
            low += 1
    
    arr[low], arr[high] = arr[high], arr[low]
    return low
    

def kthLargest(arr:list, k:int):
    
    i = 0
    j = len(arr)-1
    
    while i <= j:
        pivot_idx = partition(arr, i, j)

        #print(pivot_idx)
        # Case 1 - pivot is k-th largest number
        if pivot_idx == len(arr)-k:
            return arr[pivot_idx]
        # Case 2 - pivot is ranked lower than k
        # Look at elements to right of pivot
        elif pivot_idx < len(arr)-k:
            i = pivot_idx+1
        # Case 3 - pivot ranked higher than k
        # Look at elements to left of pivot
        elif pivot_idx > len(arr)-k:
            j = pivot_idx-1
        

# Same logic as kthLargest. look at rank k instead of rank len(arr)-k
def kthSmallest(arr:list, k:int):
    
    i = 0
    j = len(arr)-1
    
    while i <= j:
        pivot_idx = partition(arr, i, j)
        if pivot_idx == k:
            return arr[pivot_idx]
        elif pivot_idx < k:
            i = pivot_idx+1
        elif pivot_idx > k:
            j = pivot_idx -1
            


# Example 1
arr = [10, 7, 8, 9, 1, 5]
k = 3
print("Array:", arr)
n = kthLargest(arr, k)
print("K-th Largest:", n, k)
print(sorted(arr))
print()

 
            
# Example 2
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
k = 7
print("Array:", arr)
n = kthLargest(arr, k)
print("K-th Largest:", n, k)
print(sorted(arr))
print()    
            
# Example 3
for k in range(1, 10):
    arr = [5, 4, 8, 8, 8, 3, 10, 1, 21]
    print("Array:", arr, k)
    n = kthLargest(arr, k)
    print("K-th Largest:", n, k)
    print(sorted(arr))
    print()   