# Quicksort - Iterative Implementation

from collections import deque

def partition(arr:list, low:int, high:int) -> None:
    
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            arr[low], arr[j] = arr[j], arr[low]
            low += 1
            
    arr[low], arr[high] = arr[high], arr[low]
    return low


def quickSort(arr:list) -> None:
    
    # Queue holds (low, high) interval to partition 
    # Starting case is entire array
    queue = deque([(0, len(arr)-1)])
    
    while queue:
        low, high = queue.popleft()
        if low < high:        
            pivot_idx = partition(arr, low, high)
            # Add bottom portion and top portion to queue
            queue.append( (low, pivot_idx-1) )
            queue.append( (pivot_idx+1, high) )
            


# Example 1
arr = [10, 7, 8, 9, 1, 5]
print("Array:", arr)
quickSort(arr)
print("Sorted:", arr)
print()

# Example 2
arr = [5, 4, 8, 8, 8, 3, 10, 1, 21]
print("Array:", arr)
quickSort(arr)
print("Sorted:", arr)
print()       
            
# Example 3
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print("Array:", arr)
quickSort(arr)
print("Sorted:", arr)
print()                 