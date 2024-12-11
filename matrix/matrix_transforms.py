#### Useful functions to transform matrices

from typing import List

# Sample matrix
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
    [17, 18, 19, 20],
]


# Pretty print
def pprint(matrix: List[List[int]]) -> List[List[int]]:
    for r in matrix:
        print(list(r))


### Method 1 - Zip


def rotateLeft90_1(matrix: List[List[int]]) -> List[List[int]]:
    return [*zip(*matrix)][::-1]


def rotateRight90_1(matrix: List[List[int]]) -> List[List[int]]:
    return [*zip(*matrix[::-1])]


### Method 2 - Coordinates


def transpose(matrix: List[List[int]]) -> List[List[int]]:
    NROWS = len(matrix)
    NCOLS = len(matrix[0])
    """
    Flip row and col indexes
    """
    return [[matrix[r][c] for r in range(NROWS)] for c in range(NCOLS)]


def rotateLeft90_2(matrix: List[List[int]]) -> List[List[int]]:
    NROWS = len(matrix)
    NCOLS = len(matrix[0])
    """
    Can be thought of as transpose + reverse rows
    """
    return [[matrix[r][c] for r in range(NROWS)] for c in range(NCOLS - 1, -1, -1)]


def rotateRight90_2(matrix: List[List[int]]) -> List[List[int]]:
    NROWS = len(matrix)
    NCOLS = len(matrix[0])
    """
    Can be thought of as transpose + reverse columns
    """
    return [[matrix[r][c] for r in range(NROWS - 1, -1, -1)] for c in range(NCOLS)]


if __name__ == "__main__":

    print()
    print("Original Matrix")
    print()
    pprint(matrix)
    print()

    print("Transpose")
    print()
    pprint(transpose(matrix))
    print()

    print("Rotation Left")
    print()
    pprint(rotateLeft90_1(matrix))
    print()
    pprint(rotateLeft90_2(matrix))
    print()

    print("Rotation Right")
    print()
    pprint(rotateRight90_1(matrix))
    print()
    pprint(rotateRight90_2(matrix))
