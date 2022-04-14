# Egg Drop Problem


class Solution:
    
    def eggDrop(self, K: int, N: int) -> int:
		# M x K --> Given M moves and K eggs, what is the maximum floor we can check ?
        M = 300 # big enough number

        # Here DP holds number of floors we can check
        #dp[floor][eggs]
        dp = [[0 for j in range(K+1)] for i in range(M+1)]
        # Initialization 1 --> no move no floor --> dp[0][*] = 0
        # Initialization 2 --> no egg no floor --> dp[*][0] = 0
        # General case --> we want to find dp[m][k] --> we pick one egg and drop (1 move)
        #              --> now we have k or k-1 eggs, depending on whether the previous egg is broken
        #              --> so in either case, we can at least sum up 1 (first move) + dp[m-1][k] + dp[m-1][k-1] 
        for i in range(1, M+1): # Moves
            for j in range(1, K+1): # Eggs
                dp[i][j] = 1 + dp[i-1][j] + dp[i-1][j-1]
                if dp[i][j] >= N: # if we reach given floor N, then we can return number of moves
                    return i

                
                
                    

MAX = 1000
memo = [[-1 for i in range(MAX)] for j in range(MAX)]
def solveEggDrop(n, k):
 
    if (memo[n][k] != -1):
        return memo[n][k]
     
    if (k == 1 or k == 0):
        return k
 
    if (n == 1):
        return k
 
    min = float('inf')
    res = 0
 
    for x in range(1,k+1):
        res = max(solveEggDrop(n - 1, x - 1), solveEggDrop(n, k - x))
        if (res < min):
            min = res     
 
    memo[n][k] = min + 1
    return min + 1


def test1():
    n = 2
    k = 100
    s = Solution().eggDrop(n, k)
    #s = solveEggDrop(n,k)
    print(s)

test1()

#0 1 2 3 4 5 6 7 8 9 10
# i = 0, j = 10
# m=5, j=4, egg = 1
# m=2, j=1, egg = 2


