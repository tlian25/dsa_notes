# Longest Increasing Subsequence for an Array

# Dynamic Programming to track

def LIS(arr:list) -> int:
    
    # tails[n] = Smallest ending element for all possible subsequences of length n
    tails = [0 for _ in range(len(arr))]
    maxsize = 0
    
    for n in arr:
        # Binary Search to find where to place n
        i, j = 0, maxsize
        
        # We want to find the largest element in tails that we can place n behind
        # So idx s.t tails[idx-1] < n and i <= idx <= maxsize
        #
        # Case 1: n is the largest number - we can increase longest subsequence seen so far by 1. idx = maxsize
        # Case 2: n is not the largest number - we update some previous seen subsequence to end at n 
        # or alternatively, we build update longest subsequence we can build ending at n.
        
        idx = binSearch(tails, n, i, j)
        tails[idx] = n
        print(tails)
        maxsize = max(maxsize, idx+1)
        
    return maxsize

# Binary search of an array between start and end indexes
# Find largest index s.t. all previous items < n
# Non-inclusive end element
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


def test2():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = LIS(nums)
    print(s)
    assert s == 10, 'Expected s == 10'
    
test2()
        
     
