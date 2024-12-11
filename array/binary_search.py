# Binary Search of a Sorted Array


# Recursive
def binarySearch(arr: list, target: int, low: int, high: int) -> int:

    if low > high:
        return -1

    mid = (low + high) // 2
    print("mid:", mid, "arr[mid]:", arr[mid])

    # Target found
    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        # Look left half as target is < mid
        return binarySearch(arr, target, low, mid - 1)

    else:
        # Look at right half as target > mid
        return binarySearch(arr, target, mid + 1, high)


# Binary Search iterative
def binarySearch_iter(arr, target):
    l = 0
    r = len(arr)

    while l < r:
        mid = (l + r) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            r = mid
        else:
            l = mid + 1

    return -1
    # Alternatively
    # return r # for first index > than target
    # return l # for first index <= target


# Modify to handle duplicates
def binarySearch_LeftOccurrance(arr, target):
    l = 0
    r = len(arr)

    while l <= r:  # Allow equality to keep shifting
        m = (l + r) // 2
        # keep shifting right side <=
        if arr[m] >= target:
            r = m
        else:
            l = m
    return r


def binarySearch_RightOccurrance(arr, target):
    l = 0
    r = len(arr)

    while l <= r:  # Allow equality to keep shifting
        m = (l + r) // 2
        # keep shifting left side =>
        if arr[m] <= target:
            l = m
        else:
            r = m

    return l


### TESTS
arr = [2, 3, 4, 5, 10, 40, 50]
arr2 = [2, 3, 4, 5, 10, 10, 10, 10, 10, 40, 50]


def test_1():
    for i, x in enumerate(arr):
        idx = binarySearch(arr, x, 0, len(arr))
        assert idx == i


def test_2():
    for i, x in enumerate(arr):
        idx = binarySearch_iter(arr, x)
        assert idx == i


def test_3():
    x = 7
    idx = binarySearch_iter(arr, x)
    assert idx == -1


def test_4():
    x = 10
    idx = binarySearch_LeftOccurrance(arr2, x)
    assert idx == 4

    idx = binarySearch_RightOccurrance(arr2, x)
    assert idx == 8


def test_5():
    x = 40
    idx = binarySearch_LeftOccurrance(arr2, x)
    assert idx == 9

    idx = binarySearch_RightOccurrance(arr2, x)
    assert idx == 9
