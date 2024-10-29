# Egg Drop Problem
import sys

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
        for moves in range(1, M+1): # Moves
            for eggs in range(1, K+1): # Eggs
                dp[moves][eggs] = 1 + dp[moves-1][eggs] + dp[moves-1][eggs-1]
                if dp[moves][eggs] >= N: # if we reach given floor N, then we can return number of moves
                    return moves

                
                
                    

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



# Function to get minimum number of trials
# needed in worst case with n eggs and k floors
def eggDrop(eggs, floors):

    # If there are no floors, then no trials
    # needed. OR if there is one floor, one
    # trial needed.
    if (floors <= 1):
        return floors

    # We need k trials for one egg
    # and k floors
    if (eggs == 1):
        return floors

    min_trials = sys.maxsize

    # Consider all droppings from 1st
    # floor to kth floor and return
    # the minimum of these values plus 1.
    for floor in range(1, floors + 1):
        trials = max(
            # Case 1: Egg breaks -> check every floor below current floor with 1 less egg
            eggDrop(eggs - 1, floor - 1),
            # Case 2: Egg doesn't break -> check every floor above current floor with same number of eggs
            eggDrop(eggs, floors - floor)
        ) + 1  # And add 1 to trial count since we dropped at current floor
        
        min_trials = min(min_trials, trials)

    return min_trials


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


