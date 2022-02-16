# All Pairs Shortest Path

from typing import List
import numpy as np

inf = float('inf')


# Matrix graph representation
# where A0[i][j] = distance of path from i -> j
A = [[0, 3, inf, 7],
      [8, 0, 2, inf],
      [5, inf, 0, 1],
      [2, inf, inf, 0]]



# Compare direct path of previous matrix with going through a "middle" point
def relaxMatrix(matrix: List[List[int]], middle:int) -> List[List[int]]:
    
    n = len(matrix)
    
    A = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            # Take the min of:
            # - previous direct path i->j
            # - previous path i->middle->j
            A[i][j] = min(matrix[i][j], matrix[i][middle] + matrix[middle][j])
            
    return A

# Base Graph Matrix
print("Base Graph Matrix")
print(np.matrix(A))
print()


# Relax n times

# Going through 0
A0 = relaxMatrix(A, 0)
print("A0")
print(np.matrix(A0))
print()

# Going through 1
A1 = relaxMatrix(A0, 1)
print("A1")
print(np.matrix(A1))
print()

# Going through 2
A2 = relaxMatrix(A1, 2)
print("A2")
print(np.matrix(A2))
print()

# Going through 3
A3 = relaxMatrix(A2, 3)
print("A3")
print(np.matrix(A3))
print()



##### Putting it all together in a single function

def APSP(matrix: List[List[int]]) -> List[List[int]]:
    
    n = len(matrix)
    # Loop through possible middle characters
    
    for m in range(n):
        matrix = relaxMatrix(matrix, m)
        
    return matrix


apsp = APSP(A)

print("All Pairs Shortest Path")
print(np.matrix(apsp))
print()
    