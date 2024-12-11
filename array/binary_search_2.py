# Modified Binary Search to find nearest number


# Try to find lowest number >= target.
# Return Index
def binarySearchNearestLarger(arr: list, target: int) -> int:
    # need to use len(arr) which is outside if target > all numbers in arr
    # In this case, j is end of array
    i = 0
    j = len(arr)

    while i < j:
        mid = (i + j) // 2
        if arr[mid] == target:
            # Slide if duplicates found
            while mid - 1 >= 0 and arr[mid - 1] == target:
                mid -= 1
            return mid

        elif target < arr[mid]:
            j = mid
        else:
            i = mid + 1
    return j


def binarySearchNearestSmaller(arr: list, target: int) -> int:
    idx = binarySearchNearestLarger(arr, target)
    if arr[idx] == target:
        return idx
    return idx - 1


### TESTS

arr = [2, 4, 6, 8, 9, 10, 10, 10, 12, 14, 16]


def test_1():
    target = 3
    idx = binarySearchNearestLarger(arr, target)
    assert idx == 1


def test_2():
    target = 11
    idx = binarySearchNearestLarger(arr, target)
    assert idx == 8


def test_3():
    target = 10
    idx = binarySearchNearestLarger(arr, target)
    assert idx == 5


def test_4():
    target = 16
    idx = binarySearchNearestLarger(arr, target)
    assert idx == 10


def test_5():
    target = 18
    idx = binarySearchNearestLarger(arr, target)
    assert idx == 11


def test_6():
    target = 3
    idx = binarySearchNearestSmaller(arr, target)
    assert idx == 0


def test_7():
    target = 16
    idx = binarySearchNearestSmaller(arr, target)
    assert idx == 10


def test_8():
    target = 15
    idx = binarySearchNearestSmaller(arr, target)
    assert idx == 9


def test_9():
    target = 1
    idx = binarySearchNearestSmaller(arr, target)
    assert idx == -1
