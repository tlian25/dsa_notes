# Binary Search of a Sorted Array


# Recursive
def binarySearch(arr:list, low:int, high:int, target:int) -> int:
    
    if  low > high:
        return -1
    
    mid = (high+low) // 2
    
    if arr[mid] == target:
        return mid
    
    elif arr[mid] > target:
        return binarySearch(arr, low, mid-1, target)
    
    else:
        return binarySearch(arr, mid+1, high, target)
    


def binarySearch_iter(arr, target):
    i = 0
    j = len(arr)-1
    
    while i <= j:
        mid = (i+j) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            j = mid-1
        else:
            i = mid+1
            
    return -1

# Test array
arr = [ 2, 3, 4, 5, 10, 40, 50]
x = 10
 
# Function call
result = binarySearch(arr, 0, len(arr)-1, x)
print(result)


# Function call
result = binarySearch_iter(arr, x)
print(result)