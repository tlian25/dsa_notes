# Longest Increasing Subsequence for an Array

# Dynamic Programming to track
# tails[n] = Smallest element for subsequence of length n

def LIS(arr:list) -> int:
    
    tails = [0 for _ in range(len(arr))]
    maxsize = 0
    
    for n in arr:
        # Binary Search to find where to place n
        i, j = 0, maxsize
        idx = binSearch(tails, n, i, j)
        tails[idx] = n
        maxsize = max(maxsize, idx+1)
        
    return maxsize

# Binary search of an array between start and end indexes  
def binSearch(tails:list, n:int, start:int, end:int) -> int:
    
    while start < end:
        mid = (start+end) // 2
        if tails[mid] < n:
            start = mid+1
        else:
            end = mid
            
    return start



def test1():
    nums = [1,8,4,12,2,10,6,14,1,9,5,13,3,11,7,15]
    s = LIS(nums)
    print(s)
    assert s == 6, 'Expected s == 6'
    
test1()
        
     
