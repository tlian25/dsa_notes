# Egg Drop Problem
"""
The egg drop problem is a mathematical puzzle asking for the minimum number of drops,
in the worst-case scenario, to identify the "critical floor" from which an egg will
break when dropped from a building with a given number of floors and a finite number
of eggs. The puzzle involves a trade-off: more drops can be made between floors if you
have more eggs, but you lose eggs with each unsuccessful drop. 
"""


# DP approach
class Solution:
    def eggDrop(self, K: int, N: int) -> int:
        # M x K --> Given M moves and K eggs, what is the maximum floor we can check ?
        M = 300  # big enough number

        # Here DP holds number of floors we can check
        # dp[floor][eggs]
        dp = [[0 for j in range(K + 1)] for i in range(M + 1)]
        # Initialization 1 --> no move no floor --> dp[0][*] = 0
        # Initialization 2 --> no egg no floor --> dp[*][0] = 0
        # General case --> we want to find dp[m][k] --> we pick one egg and drop (1 move)
        #              --> now we have k or k-1 eggs, depending on whether the previous egg is broken
        #              --> so in either case, we can at least sum up 1 (first move) + dp[m-1][k] + dp[m-1][k-1]
        for moves in range(1, M + 1):  # Moves
            for eggs in range(1, K + 1):  # Eggs
                dp[moves][eggs] = 1 + dp[moves - 1][eggs] + dp[moves - 1][eggs - 1]
                if dp[moves][eggs] >= N:
                    # if we reach given floor N, then we can return number of moves
                    return moves


# Method 2 - Same DP approach without solution class
MAX = 1000
memo = [[-1 for i in range(MAX)] for j in range(MAX)]


def solveEggDrop(n, k):

    if memo[n][k] != -1:
        return memo[n][k]

    if k == 1 or k == 0:
        return k

    if n == 1:
        return k

    min = float("inf")
    res = 0

    for x in range(1, k + 1):
        res = max(solveEggDrop(n - 1, x - 1), solveEggDrop(n, k - x))
        if res < min:
            min = res

    memo[n][k] = min + 1
    return min + 1


def test1():
    n = 2
    k = 100
    s1 = Solution().eggDrop(n, k)
    assert s1 == 14

def test2():
    n = 2
    k = 100
    s2 = solveEggDrop(n, k)
    assert s2 == 14

test1()
test2()

# 0 1 2 3 4 5 6 7 8 9 10
# i = 0, j = 10
# m=5, j=4, egg = 1
# m=2, j=1, egg = 2
