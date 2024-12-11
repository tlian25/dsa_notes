# Binary Indexed Trees (Fenwick Trees)

"""
Provides a way to represent an array of numbers in a tree array,
allowing prefix sums to be calculated efficiently

"""

# Example 1

a = [2, 1, 4, 6, -1, 5, -32, 0, 1]


def update(idx, val):
    a[idx] = val


for i in range(100):
    print(i, (i & -i))
